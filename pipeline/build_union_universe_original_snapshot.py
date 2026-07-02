#!/usr/bin/env python3
"""Build a defensible economically significant final-rule universe.

Definition used here:
- discovery comes from official determination sources, not keyword extraction:
  Unified Agenda priority values, RegInfo/OIRA target records, and RegStats
  FR tracking rows;
- the matched Federal Register item must be a RULE with a final-like action;
- corrections, stays, delays, withdrawals, temporary rules, and interim final
  rules are audit rows, not primary rows;
- the audited primary universe requires CFR metadata from local FR parsing;
- provisional rows are kept when a source says final/econ but local FR XML
  coverage is not available to validate CFR metadata.

The rule-level file collapses same-presidential-year documents connected by a
shared RIN into one row, while retaining all related FR document keys and titles
for audit.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

import pandas as pd


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
ROOT = PACKAGE_ROOT
OUT = PACKAGE_ROOT / "generated_outputs" / "direct_snapshot_run" / "econ_sig_final_rule_universe_v2"
MIN_PRESIDENTIAL_YEAR = 2000
MAX_PRESIDENTIAL_YEAR = 2024

SOURCE_INPUTS = PACKAGE_ROOT / "source_inputs"
FR_RAW = SOURCE_INPUTS / "fr_final_rules_rawparsed.csv.gz"
FR_RIN = SOURCE_INPUTS / "fr_final_rules_rin_exploded.csv.gz"
UA_ALL = SOURCE_INPUTS / "ua_all_flat_rin_norm.csv.gz"

STRICT_LINKED = SOURCE_INPUTS / "econ_sig_final_rules_STRICT_FR_RULE_2000_forward_linked_full.csv"
REGSTATS_COUNTS = SOURCE_INPUTS / "econ_significant_rules_by_presidential_year.csv"

ECON_PRIORITY_VALUES = {"Economically Significant", "Section 3(f)(1) Significant"}
PRIMARY_ACTION_FAMILIES = {"ordinary_final", "direct_final_initial"}


def clean(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except (TypeError, ValueError):
        pass
    return re.sub(r"\s+", " ", str(value)).strip()


def abridge(value: Any, limit: int = 900) -> str:
    text = clean(value)
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + " ..."


def pipe_join(values: Any) -> str:
    out: list[str] = []
    for value in values:
        text = clean(value)
        if text and text not in out:
            out.append(text)
    return " | ".join(out)


def doc_key(date_value: Any, frdoc_value: Any) -> str:
    date_text = clean(date_value)
    frdoc = clean(frdoc_value)
    if not date_text or not frdoc:
        return ""
    return f"{date_text}__FRDOC_{frdoc}"


def presidential_year(date_value: Any) -> Any:
    dt = pd.to_datetime(date_value, errors="coerce")
    if pd.isna(dt):
        return pd.NA
    return int(dt.year if dt.month >= 2 else dt.year - 1)


def split_rins(value: Any) -> list[str]:
    text = clean(value).upper()
    if not text:
        return []
    found = re.findall(r"\b\d{4}-[A-Z0-9]{2}\d{2}\b", text)
    return sorted(set(found))


def title_score(left: Any, right: Any) -> float:
    a = clean(left).lower()
    b = clean(right).lower()
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def classify_action(action: Any) -> str:
    text = clean(action).lower()
    if not text:
        return "other_rule_no_final_word"
    if "direct final" in text:
        if re.search(
            r"confirmation|effective date|compliance date|correction|technical|"
            r"withdraw|change to submission|notice of stay",
            text,
        ):
            return "direct_final_support"
        return "direct_final_initial"
    if "interim" in text:
        return "interim_final_or_interim"
    if "temporary" in text:
        return "temporary_final"
    if re.search(r"correction|correcting|correct |technical amendment", text):
        return "correction_technical"
    if re.search(r"delay|stay|postpone|extension|extend|effective date", text):
        return "delay_stay_extension"
    if re.search(r"withdraw|removal|remove", text):
        return "withdraw_remove"
    if "final" in text:
        return "ordinary_final"
    return "other_rule_no_final_word"


def exclusion_reason(action_family: str) -> str:
    if action_family in PRIMARY_ACTION_FAMILIES:
        return ""
    return {
        "correction_technical": "not_primary_correction_or_technical",
        "delay_stay_extension": "not_primary_delay_stay_extension_or_effective_date",
        "direct_final_support": "not_primary_direct_final_confirmation_or_support",
        "interim_final_or_interim": "not_primary_interim_final_or_interim",
        "temporary_final": "not_primary_temporary_final",
        "withdraw_remove": "not_primary_withdrawal_or_removal",
        "other_rule_no_final_word": "not_primary_no_final_action_signal",
    }.get(action_family, "not_primary_other_action_family")


def load_fr_docs() -> pd.DataFrame:
    raw = pd.read_csv(FR_RAW, dtype=str, low_memory=False)
    raw["fr_doc_key"] = [doc_key(d, n) for d, n in zip(raw["fr_issue_date"], raw["fr_frdoc_no"])]
    raw["presidential_year"] = raw["fr_issue_date"].map(presidential_year).astype("Int64")
    raw["action_family"] = raw["fr_action"].map(classify_action)
    raw["fr_cfr_count_num"] = pd.to_numeric(raw["fr_cfr_count"], errors="coerce").fillna(0).astype(int)
    subagency_cfr = raw["fr_subagency"].fillna("").astype(str).str.contains(
        r"\b\d+\s+CFR\s+Parts?\b", flags=re.IGNORECASE, regex=True
    )
    raw.loc[raw["fr_cfr"].fillna("").astype(str).str.strip().eq("") & subagency_cfr, "fr_cfr"] = raw[
        "fr_subagency"
    ]
    raw["local_fr_cfr_validated"] = (raw["fr_cfr_count_num"] > 0) | subagency_cfr
    raw = raw[raw["fr_doc_key"].ne("")].copy()
    raw = raw.drop_duplicates("fr_doc_key", keep="first")

    rin = pd.read_csv(FR_RIN, dtype=str, low_memory=False)
    rin["fr_doc_key"] = [doc_key(d, n) for d, n in zip(rin["fr_issue_date"], rin["fr_frdoc_no"])]
    rin_group = (
        rin[rin["fr_doc_key"].ne("")]
        .groupby("fr_doc_key")
        .agg(
            local_fr_rin_list=("rin_norm", lambda s: pipe_join(sorted(set(clean(x).upper() for x in s if clean(x))))),
            local_fr_rin_count=("rin_norm", lambda s: len(set(clean(x).upper() for x in s if clean(x)))),
        )
        .reset_index()
    )
    raw = raw.merge(rin_group, on="fr_doc_key", how="left")
    raw["local_fr_rin_list"] = raw["local_fr_rin_list"].fillna("")
    raw["local_fr_rin_count"] = raw["local_fr_rin_count"].fillna(0).astype(int)
    return raw


def load_ua_econ() -> tuple[pd.DataFrame, set[str], dict[str, dict[str, str]]]:
    ua = pd.read_csv(UA_ALL, dtype=str, low_memory=False)
    ua = ua[
        ua["ua_priority_category"].isin(ECON_PRIORITY_VALUES)
        & ua["rin_norm"].fillna("").astype(str).str.strip().ne("")
    ].copy()
    ua["rin_norm"] = ua["rin_norm"].str.upper()
    agg = (
        ua.groupby("rin_norm")
        .agg(
            ua_econ_priority_values=("ua_priority_category", pipe_join),
            ua_rule_titles=("ua_rule_title", pipe_join),
            ua_agencies=("ua_agency_name", pipe_join),
            ua_parent_agencies=("ua_parent_agency_name", pipe_join),
            ua_rule_stages=("ua_rule_stage", pipe_join),
            ua_final_rule_dates=("ua_final_rule_dates", pipe_join),
            ua_nprm_dates=("ua_nprm_dates", pipe_join),
            ua_cfr_list=("ua_cfr_list", pipe_join),
            ua_timetable_summary=("ua_timetable_summary", pipe_join),
            ua_abstract=("ua_abstract", pipe_join),
            ua_vintages=("ua_vintage", pipe_join),
        )
        .reset_index()
    )
    agg["ua_abstract_abridged"] = agg["ua_abstract"].map(abridge)
    by_rin = {row["rin_norm"]: row.to_dict() for _, row in agg.iterrows()}
    return agg, set(agg["rin_norm"]), by_rin


def load_strict_linked() -> pd.DataFrame:
    strict = pd.read_csv(STRICT_LINKED, dtype=str, low_memory=False)
    strict["fr_doc_key"] = [
        doc_key(d, n) for d, n in zip(strict["fr_publication_date"], strict["fr_document_number"])
    ]
    strict["presidential_year"] = pd.to_numeric(strict["presidential_year"], errors="coerce").astype("Int64")
    strict["action_family"] = strict["fr_action"].map(classify_action)
    strict["strict_rin_list"] = strict.apply(
        lambda row: pipe_join(split_rins(row.get("rin_list", "")) or split_rins(row.get("rin_primary", ""))),
        axis=1,
    )
    strict["strict_fr_cfr_validated"] = strict["fr_cfr"].fillna("").astype(str).str.strip().ne("")
    strict = strict[strict["fr_doc_key"].ne("")].copy()
    return strict


def build_document_candidates(fr: pd.DataFrame, ua_econ_rins: set[str], strict: pd.DataFrame) -> pd.DataFrame:
    ua_doc_keys: set[str] = set()
    for _, row in fr.iterrows():
        if any(rin in ua_econ_rins for rin in split_rins(row.get("local_fr_rin_list", ""))):
            ua_doc_keys.add(row["fr_doc_key"])

    strict_primary = strict[
        strict["official_fr_type"].fillna("").str.lower().eq("rule")
        & strict["action_family"].isin(PRIMARY_ACTION_FAMILIES)
    ].copy()
    strict_doc_keys = set(strict_primary["fr_doc_key"])

    strict_by_key = {
        key: grp.copy() for key, grp in strict_primary.groupby("fr_doc_key", dropna=False)
    }
    fr_by_key = fr.set_index("fr_doc_key", drop=False)
    fr_by_date: dict[str, pd.DataFrame] = {
        date: grp.copy() for date, grp in fr.groupby("fr_issue_date", dropna=False)
    }

    all_doc_keys = sorted(ua_doc_keys | strict_doc_keys)
    rows: list[dict[str, Any]] = []
    for key in all_doc_keys:
        has_local = key in fr_by_key.index
        strict_grp = strict_by_key.get(key)
        local_fallback = None
        local_fallback_score = 0.0
        if not has_local and strict_grp is not None:
            strict_src = strict_grp.iloc[0]
            strict_rins = set(
                split_rins(strict_src.get("strict_rin_list", ""))
                or split_rins(strict_src.get("rin_list", ""))
                or split_rins(strict_src.get("rin_primary", ""))
            )
            same_day = fr_by_date.get(clean(strict_src.get("fr_publication_date", "")))
            if same_day is not None and strict_rins:
                cand = same_day[
                    same_day["local_fr_rin_list"].map(lambda value: bool(strict_rins.intersection(split_rins(value))))
                ].copy()
                if not cand.empty:
                    cand["_title_score"] = cand["fr_subject"].map(
                        lambda value: title_score(value, strict_src.get("fr_title", ""))
                    )
                    cand = cand.sort_values(["_title_score", "local_fr_cfr_validated"], ascending=[False, False])
                    if len(cand) == 1 or float(cand.iloc[0]["_title_score"]) >= 0.55:
                        local_fallback = cand.iloc[0]
                        local_fallback_score = float(cand.iloc[0]["_title_score"])
        if has_local:
            src = fr_by_key.loc[key]
            if isinstance(src, pd.DataFrame):
                src = src.iloc[0]
            row = {
                "fr_doc_key": key,
                "fr_issue_date": src.get("fr_issue_date", ""),
                "fr_frdoc_no": src.get("fr_frdoc_no", ""),
                "presidential_year": src.get("presidential_year", pd.NA),
                "fr_doc_type": src.get("fr_doc_type", ""),
                "fr_subject": src.get("fr_subject", ""),
                "fr_action": src.get("fr_action", ""),
                "action_family": src.get("action_family", ""),
                "fr_agency_header": src.get("fr_agency_header", ""),
                "fr_agency": src.get("fr_agency", ""),
                "fr_subagency": src.get("fr_subagency", ""),
                "fr_cfr": src.get("fr_cfr", ""),
                "fr_cfr_count": src.get("fr_cfr_count", ""),
                "fr_start_page": src.get("fr_start_page", ""),
                "fr_end_page": src.get("fr_end_page", ""),
                "fr_summary": src.get("fr_summary", ""),
                "local_fr_rin_list": src.get("local_fr_rin_list", ""),
                "local_fr_cfr_validated": bool(src.get("local_fr_cfr_validated", False)),
                "found_in_local_fr": True,
                "local_fallback_fr_doc_key": "",
                "local_fallback_title_score": "",
            }
        else:
            src = strict_grp.iloc[0]
            row = {
                "fr_doc_key": key,
                "fr_issue_date": src.get("fr_publication_date", ""),
                "fr_frdoc_no": src.get("fr_document_number", ""),
                "presidential_year": src.get("presidential_year", pd.NA),
                "fr_doc_type": src.get("official_fr_type", ""),
                "fr_subject": src.get("fr_title", ""),
                "fr_action": src.get("fr_action", ""),
                "action_family": src.get("action_family", ""),
                "fr_agency_header": (
                    local_fallback.get("fr_agency_header", "")
                    if local_fallback is not None
                    else src.get("fr_agency_header", "")
                ),
                "fr_agency": src.get("fr_tracking_agency", ""),
                "fr_subagency": "",
                "fr_cfr": local_fallback.get("fr_cfr", "") if local_fallback is not None else src.get("fr_cfr", ""),
                "fr_cfr_count": (
                    local_fallback.get("fr_cfr_count", "") if local_fallback is not None else ""
                ),
                "fr_start_page": "",
                "fr_end_page": "",
                "fr_summary": src.get("fr_summary", ""),
                "local_fr_rin_list": (
                    local_fallback.get("local_fr_rin_list", "") if local_fallback is not None else ""
                ),
                "local_fr_cfr_validated": (
                    bool(local_fallback.get("local_fr_cfr_validated", False))
                    if local_fallback is not None
                    else False
                ),
                "found_in_local_fr": local_fallback is not None,
                "local_fallback_fr_doc_key": (
                    local_fallback.get("fr_doc_key", "") if local_fallback is not None else ""
                ),
                "local_fallback_title_score": (
                    f"{local_fallback_score:.3f}" if local_fallback is not None else ""
                ),
            }

        strict_rins: list[str] = []
        strict_titles: list[str] = []
        strict_sources: list[str] = []
        strict_cfr_validated = False
        if strict_grp is not None:
            strict_rins = sorted(set(r for value in strict_grp["strict_rin_list"] for r in split_rins(value)))
            strict_titles = [clean(x) for x in strict_grp["oira_title"] if clean(x)]
            strict_sources = [clean(x) for x in strict_grp["source_system"] if clean(x)]
            strict_cfr_validated = bool(strict_grp["strict_fr_cfr_validated"].any())

        all_rins = sorted(set(split_rins(row["local_fr_rin_list"]) + strict_rins))
        econ_rins = sorted(r for r in all_rins if r in ua_econ_rins or strict_grp is not None)

        row.update(
            {
                "candidate_rin_list": pipe_join(all_rins),
                "candidate_econ_rin_list": pipe_join(econ_rins),
                "source_ua_any_econ_rin": key in ua_doc_keys,
                "source_regstats_oira_linked": key in strict_doc_keys,
                "source_systems": pipe_join(strict_sources + (["ua_any_econ_rin"] if key in ua_doc_keys else [])),
                "oira_regstats_titles": pipe_join(strict_titles),
                "strict_fr_cfr_validated": strict_cfr_validated,
            }
        )
        row["final_like_action"] = row["action_family"] in PRIMARY_ACTION_FAMILIES
        row["primary_exclusion_reason"] = exclusion_reason(row["action_family"])
        row["cfr_validation_status"] = (
            "validated_local_fr_cfr"
            if row["local_fr_cfr_validated"]
            else ("validated_strict_fr_cfr" if row["strict_fr_cfr_validated"] else "not_validated_missing_cfr_metadata")
        )
        row["audited_primary"] = bool(row["final_like_action"] and row["local_fr_cfr_validated"])
        row["provisional_primary"] = bool(row["final_like_action"] and not row["local_fr_cfr_validated"])
        row["fr_summary_abridged"] = abridge(row["fr_summary"])
        rows.append(row)

    docs = pd.DataFrame(rows)
    docs = docs[docs["final_like_action"]].copy()
    docs["presidential_year"] = pd.to_numeric(docs["presidential_year"], errors="coerce").astype("Int64")
    return docs


class DisjointSet:
    def __init__(self) -> None:
        self.parent: dict[str, str] = {}

    def find(self, item: str) -> str:
        self.parent.setdefault(item, item)
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, left: str, right: str) -> None:
        self.parent[self.find(right)] = self.find(left)


def add_rule_groups(docs: pd.DataFrame) -> pd.DataFrame:
    dsu = DisjointSet()
    by_year_rin: dict[tuple[str, str], str] = {}
    for _, row in docs.iterrows():
        doc = row["fr_doc_key"]
        dsu.find(doc)
        year = clean(row.get("presidential_year", ""))
        for rin in split_rins(row.get("candidate_econ_rin_list", "")):
            key = (year, rin)
            if key in by_year_rin:
                dsu.union(doc, by_year_rin[key])
            else:
                by_year_rin[key] = doc
    docs = docs.copy()
    docs["rule_group_key"] = docs["fr_doc_key"].map(dsu.find)
    return docs


def score_representative(row: pd.Series) -> tuple[int, str]:
    score = 0
    if bool(row.get("source_regstats_oira_linked", False)):
        score += 100
    if bool(row.get("source_ua_any_econ_rin", False)):
        score += 40
    if bool(row.get("local_fr_cfr_validated", False)):
        score += 20
    if clean(row.get("action_family", "")) == "ordinary_final":
        score += 10
    return (-score, clean(row.get("fr_issue_date", "")))


def build_rule_level(docs: pd.DataFrame, ua_by_rin: dict[str, dict[str, str]]) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for group_key, grp in docs.sort_values(["fr_issue_date", "fr_doc_key"]).groupby("rule_group_key", sort=False):
        scored = grp.copy()
        scored["_score_key"] = scored.apply(score_representative, axis=1)
        rep = scored.sort_values("_score_key").iloc[0]
        all_rins = sorted(set(r for value in grp["candidate_econ_rin_list"] for r in split_rins(value)))

        ua_parts = [ua_by_rin[r] for r in all_rins if r in ua_by_rin]
        out = {
            "rule_group_key": group_key,
            "presidential_year": rep.get("presidential_year", pd.NA),
            "representative_fr_doc_key": rep.get("fr_doc_key", ""),
            "representative_fr_issue_date": rep.get("fr_issue_date", ""),
            "representative_fr_frdoc_no": rep.get("fr_frdoc_no", ""),
            "representative_fr_title": rep.get("fr_subject", ""),
            "representative_fr_action": rep.get("fr_action", ""),
            "representative_action_family": rep.get("action_family", ""),
            "representative_fr_agency_header": rep.get("fr_agency_header", ""),
            "representative_fr_cfr": rep.get("fr_cfr", ""),
            "representative_fr_summary": rep.get("fr_summary", ""),
            "representative_fr_summary_abridged": rep.get("fr_summary_abridged", ""),
            "econ_rin_list": pipe_join(all_rins),
            "source_ua_any_econ_rin": bool(grp["source_ua_any_econ_rin"].any()),
            "source_regstats_oira_linked": bool(grp["source_regstats_oira_linked"].any()),
            "source_systems": pipe_join(x for x in grp["source_systems"]),
            "cfr_validation_statuses": pipe_join(x for x in grp["cfr_validation_status"]),
            "audited_primary": bool(grp["audited_primary"].any()),
            "provisional_primary": bool((~grp["audited_primary"]).all() and grp["provisional_primary"].any()),
            "related_fr_doc_count": int(grp["fr_doc_key"].nunique()),
            "related_fr_doc_keys": pipe_join(grp["fr_doc_key"]),
            "related_fr_dates": pipe_join(grp["fr_issue_date"]),
            "related_fr_titles": pipe_join(grp["fr_subject"]),
            "related_fr_actions": pipe_join(grp["fr_action"]),
            "related_fr_cfrs": pipe_join(grp["fr_cfr"]),
            "related_source_flags": pipe_join(
                [
                    f"{row.fr_doc_key}:"
                    f"{'UA' if row.source_ua_any_econ_rin else ''}"
                    f"{'+' if row.source_ua_any_econ_rin and row.source_regstats_oira_linked else ''}"
                    f"{'REGSTATS_OIRA' if row.source_regstats_oira_linked else ''}"
                    for row in grp.itertuples()
                ]
            ),
            "ua_econ_priority_values": pipe_join(p.get("ua_econ_priority_values", "") for p in ua_parts),
            "ua_rule_titles": pipe_join(p.get("ua_rule_titles", "") for p in ua_parts),
            "ua_agencies": pipe_join(p.get("ua_agencies", "") for p in ua_parts),
            "ua_parent_agencies": pipe_join(p.get("ua_parent_agencies", "") for p in ua_parts),
            "ua_rule_stages": pipe_join(p.get("ua_rule_stages", "") for p in ua_parts),
            "ua_final_rule_dates": pipe_join(p.get("ua_final_rule_dates", "") for p in ua_parts),
            "ua_nprm_dates": pipe_join(p.get("ua_nprm_dates", "") for p in ua_parts),
            "ua_cfr_list": pipe_join(p.get("ua_cfr_list", "") for p in ua_parts),
            "ua_timetable_summary": pipe_join(p.get("ua_timetable_summary", "") for p in ua_parts),
            "ua_abstract_abridged": pipe_join(p.get("ua_abstract_abridged", "") for p in ua_parts),
            "oira_regstats_titles": pipe_join(grp["oira_regstats_titles"]),
        }
        rows.append(out)
    rules = pd.DataFrame(rows)
    rules["presidential_year"] = pd.to_numeric(rules["presidential_year"], errors="coerce").astype("Int64")
    return rules.sort_values(["presidential_year", "representative_fr_issue_date", "representative_fr_doc_key"])


def load_benchmark_counts() -> pd.DataFrame:
    counts = pd.read_csv(REGSTATS_COUNTS)
    counts = counts.rename(
        columns={
            "Presidential Year (February 1 - January 31)": "presidential_year",
            "Economically Significant Rules Published": "regstats_benchmark_count",
        }
    )
    counts = counts[["presidential_year", "regstats_benchmark_count"]]
    counts["presidential_year"] = counts["presidential_year"].astype("Int64")
    counts["regstats_benchmark_count"] = counts["regstats_benchmark_count"].astype(int)
    return counts


def build_counts(docs: pd.DataFrame, rules: pd.DataFrame) -> pd.DataFrame:
    years = pd.DataFrame({"presidential_year": range(MIN_PRESIDENTIAL_YEAR, MAX_PRESIDENTIAL_YEAR + 1)})
    counts = years.merge(load_benchmark_counts(), on="presidential_year", how="left")
    counts["document_candidates_all"] = counts["presidential_year"].map(
        docs.groupby("presidential_year")["fr_doc_key"].nunique()
    )
    counts["document_candidates_audited_cfr"] = counts["presidential_year"].map(
        docs[docs["audited_primary"]].groupby("presidential_year")["fr_doc_key"].nunique()
    )
    counts["rule_groups_all_with_provisional"] = counts["presidential_year"].map(
        rules.groupby("presidential_year")["rule_group_key"].nunique()
    )
    counts["rule_groups_audited_cfr"] = counts["presidential_year"].map(
        rules[rules["audited_primary"]].groupby("presidential_year")["rule_group_key"].nunique()
    )
    counts["rule_groups_provisional_only"] = counts["presidential_year"].map(
        rules[rules["provisional_primary"]].groupby("presidential_year")["rule_group_key"].nunique()
    )
    for col in [
        "document_candidates_all",
        "document_candidates_audited_cfr",
        "rule_groups_all_with_provisional",
        "rule_groups_audited_cfr",
        "rule_groups_provisional_only",
    ]:
        counts[col] = counts[col].fillna(0).astype(int)
    counts["audited_rule_groups_minus_benchmark"] = (
        counts["rule_groups_audited_cfr"] - counts["regstats_benchmark_count"]
    )
    counts["all_rule_groups_minus_benchmark"] = (
        counts["rule_groups_all_with_provisional"] - counts["regstats_benchmark_count"]
    )
    return counts


def write_report(docs: pd.DataFrame, rules: pd.DataFrame, counts: pd.DataFrame) -> None:
    dup = rules[rules["related_fr_doc_count"] > 1]
    lines: list[str] = []
    lines.append("# Economically Significant Final-Rule Universe v2\n\n")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    lines.append(f"Scope: presidential years {MIN_PRESIDENTIAL_YEAR}-{MAX_PRESIDENTIAL_YEAR}.\n\n")
    lines.append("## Definition\n\n")
    lines.append(
        "Discovery uses UA econ/3(f)(1) priority and RegStats/OIRA linked target rows. "
        "The primary Federal Register filter keeps final-like RULE documents and excludes "
        "interim, temporary, correction, delay/stay/effective-date, withdrawal/removal, "
        "and direct-final support actions from the primary universe.\n\n"
    )
    lines.append("## Counts\n\n")
    lines.append(f"- Document candidates, all sources: {docs['fr_doc_key'].nunique():,}\n")
    lines.append(f"- Document candidates with local CFR validation: {docs[docs['audited_primary']]['fr_doc_key'].nunique():,}\n")
    lines.append(f"- Collapsed rule groups, all/provisional included: {rules['rule_group_key'].nunique():,}\n")
    lines.append(f"- Collapsed rule groups with local CFR validation: {rules[rules['audited_primary']]['rule_group_key'].nunique():,}\n")
    lines.append(f"- Collapsed groups with >1 related FR document: {len(dup):,}\n\n")
    lines.append("## Source Mix, Document Candidates\n\n")
    mix = docs.assign(
        source_mix=docs.apply(
            lambda r: (
                "both"
                if r["source_ua_any_econ_rin"] and r["source_regstats_oira_linked"]
                else ("ua_only" if r["source_ua_any_econ_rin"] else "regstats_oira_only")
            ),
            axis=1,
        )
    )["source_mix"].value_counts()
    lines.append("| Source mix | Docs |\n|---|---:|\n")
    for label, n in mix.items():
        lines.append(f"| {label} | {int(n)} |\n")
    lines.append("\n## Counts By Presidential Year\n\n")
    lines.append(
        "| Year | Benchmark | Docs all | Docs CFR-audited | Rule groups all | Rule groups CFR-audited | Audited Diff |\n"
    )
    lines.append("|---:|---:|---:|---:|---:|---:|---:|\n")
    for _, row in counts.iterrows():
        lines.append(
            f"| {int(row.presidential_year)} | {int(row.regstats_benchmark_count)} | "
            f"{int(row.document_candidates_all)} | {int(row.document_candidates_audited_cfr)} | "
            f"{int(row.rule_groups_all_with_provisional)} | {int(row.rule_groups_audited_cfr)} | "
            f"{int(row.audited_rule_groups_minus_benchmark)} |\n"
        )
    lines.append("\n## Out-of-Scope Rows\n\n")
    lines.append(
        "Presidential year 2025 and the January 2000 row that maps to presidential year 1999 "
        "are excluded from the working universe. Those rows are retained only in "
        "`excluded_out_of_scope_presidential_years_audit.csv`.\n"
    )
    (OUT / "README_report.md").write_text("".join(lines))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fr = load_fr_docs()
    _, ua_econ_rins, ua_by_rin = load_ua_econ()
    strict = load_strict_linked()
    docs = build_document_candidates(fr, ua_econ_rins, strict)
    docs = add_rule_groups(docs)
    rules = build_rule_level(docs, ua_by_rin)
    in_scope_years = set(range(MIN_PRESIDENTIAL_YEAR, MAX_PRESIDENTIAL_YEAR + 1))
    excluded_docs = docs[~docs["presidential_year"].isin(in_scope_years)].copy()
    excluded_rule_keys = set(excluded_docs["rule_group_key"])
    docs = docs[docs["presidential_year"].isin(in_scope_years)].copy()
    rules = rules[rules["presidential_year"].isin(in_scope_years)].copy()
    counts = build_counts(docs, rules)

    docs.to_csv(OUT / "econ_sig_final_rule_document_candidates_2000_2024.csv", index=False)
    rules.to_csv(OUT / "econ_sig_final_rules_rule_level_2000_2024.csv", index=False)
    rules[rules["audited_primary"]].to_csv(
        OUT / "econ_sig_final_rules_rule_level_2000_2024_cfr_audited.csv", index=False
    )
    rules[rules["related_fr_doc_count"] > 1].to_csv(
        OUT / "econ_sig_final_rules_multi_document_groups_audit.csv", index=False
    )
    docs[~docs["audited_primary"]].to_csv(
        OUT / "econ_sig_final_rule_provisional_or_uncfr_validated_docs_audit.csv", index=False
    )
    excluded_docs.to_csv(OUT / "excluded_out_of_scope_presidential_years_audit.csv", index=False)
    counts.to_csv(OUT / "econ_sig_final_rule_counts_vs_regstats.csv", index=False)
    write_report(docs, rules, counts)

    profile = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "document_candidates_all": int(docs["fr_doc_key"].nunique()),
        "document_candidates_cfr_audited": int(docs[docs["audited_primary"]]["fr_doc_key"].nunique()),
        "rule_groups_all_with_provisional": int(rules["rule_group_key"].nunique()),
        "rule_groups_cfr_audited": int(rules[rules["audited_primary"]]["rule_group_key"].nunique()),
        "multi_document_rule_groups": int((rules["related_fr_doc_count"] > 1).sum()),
        "excluded_out_of_scope_doc_candidates": int(len(excluded_docs)),
        "excluded_out_of_scope_rule_groups": int(len(excluded_rule_keys)),
        "presidential_year_min": MIN_PRESIDENTIAL_YEAR,
        "presidential_year_max": MAX_PRESIDENTIAL_YEAR,
        "outputs": sorted(p.name for p in OUT.iterdir() if p.is_file()),
    }
    (OUT / "profile.json").write_text(json.dumps(profile, indent=2))
    print(json.dumps(profile, indent=2))


if __name__ == "__main__":
    main()
