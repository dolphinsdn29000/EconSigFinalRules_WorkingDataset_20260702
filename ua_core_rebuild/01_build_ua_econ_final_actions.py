#!/usr/bin/env python3
"""Build a conservative UA-side base of economically significant final actions.

This is intentionally upstream of any Federal Register matching.  The output
unit is a Unified Agenda timetable final-action candidate, collapsed only across
duplicate UA vintages that repeat the same RIN/action/date event.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_INPUTS = PROJECT_ROOT / "source_inputs"
UA_SOURCE = SOURCE_INPUTS / "ua_all_flat_rin_norm.csv.gz"
OUTPUT_DIR = PROJECT_ROOT / "generated_outputs" / "ua_core_rebuild_step1"
DOCS_DIR = PROJECT_ROOT / "docs"

START_YEAR = 2000
END_YEAR = 2024
ECON_LEGACY = "Economically Significant"
ECON_3F1 = "Section 3(f)(1) Significant"
ECON_PRIORITY_VALUES = {ECON_LEGACY, ECON_3F1}
FINAL_OR_COMPLETED_STAGES = {"Final Rule Stage", "Completed Actions"}

BASE_COLUMNS = [
    "ua_base_id",
    "rin_norm",
    "ua_priority_category",
    "ua_priority_economically_significant_legacy",
    "ua_priority_section_3f1",
    "ua_priority_economic_prong",
    "ua_rule_title",
    "ua_agency_name",
    "ua_parent_agency_name",
    "ua_rule_stage",
    "ua_vintage",
    "final_action_label",
    "final_action_date_raw",
    "final_action_date_parsed",
    "final_action_year",
    "final_action_fr_citation_raw",
    "final_action_fr_volume",
    "final_action_fr_page",
    "final_action_document_number_if_available",
    "ua_timetable_source_text",
    "parser_confidence",
    "parser_notes",
    "source_row_count_collapsed",
    "source_vintages_collapsed",
]


def clean(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except (TypeError, ValueError):
        pass
    return re.sub(r"\s+", " ", str(value)).strip()


def pipe_join(values: Any) -> str:
    out: list[str] = []
    for value in values:
        text = clean(value)
        if text and text not in out:
            out.append(text)
    return " | ".join(out)


def parse_timetable_json(value: Any) -> tuple[list[dict[str, str]], str]:
    text = clean(value)
    if not text:
        return [], "missing_timetable_json"
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return [], "unparseable_timetable_json"
    if not isinstance(parsed, list):
        return [], "timetable_json_not_list"
    events: list[dict[str, str]] = []
    for item in parsed:
        if not isinstance(item, dict):
            continue
        events.append(
            {
                "action": clean(item.get("action")),
                "date": clean(item.get("date")),
                "fr_citation": clean(item.get("fr_citation")),
            }
        )
    return events, ""


def parse_ua_date(value: Any) -> dict[str, Any]:
    """Parse UA timetable dates without pretending partial dates are exact."""
    raw = clean(value)
    result = {
        "raw": raw,
        "date_parsed": "",
        "year": pd.NA,
        "granularity": "missing",
        "date_note": "",
    }
    if not raw:
        result["date_note"] = "missing_date"
        return result
    if re.search(r"to be determined|tbd|undetermined", raw, flags=re.IGNORECASE):
        result["granularity"] = "undetermined"
        result["date_note"] = "date_to_be_determined"
        return result

    exact = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{4})", raw)
    if exact:
        month, day, year = map(int, exact.groups())
        result["year"] = year
        if month == 0 and day == 0:
            result["granularity"] = "year"
            result["date_note"] = "year_only_zero_month_day"
            return result
        if day == 0 and 1 <= month <= 12:
            result["granularity"] = "month"
            result["date_note"] = "month_year_only_zero_day"
            return result
        try:
            dt = pd.Timestamp(year=year, month=month, day=day)
        except ValueError:
            result["granularity"] = "invalid"
            result["date_note"] = "invalid_calendar_date"
            return result
        result["date_parsed"] = dt.strftime("%Y-%m-%d")
        result["granularity"] = "day"
        return result

    month_year = re.fullmatch(r"(\d{1,2})/(\d{4})", raw)
    if month_year:
        month, year = map(int, month_year.groups())
        result["year"] = year
        if 1 <= month <= 12:
            result["granularity"] = "month"
            result["date_note"] = "month_year_only"
        else:
            result["granularity"] = "invalid"
            result["date_note"] = "invalid_month_year"
        return result

    year_only = re.fullmatch(r"(\d{4})", raw)
    if year_only:
        result["year"] = int(year_only.group(1))
        result["granularity"] = "year"
        result["date_note"] = "year_only"
        return result

    year_match = re.search(r"\b(19|20)\d{2}\b", raw)
    if year_match:
        result["year"] = int(year_match.group(0))
        result["granularity"] = "unstructured_year"
        result["date_note"] = "year_extracted_from_unstructured_date"
        return result

    result["granularity"] = "unparseable"
    result["date_note"] = "date_unparseable"
    return result


def parse_fr_citation(value: Any) -> tuple[str, str]:
    text = clean(value)
    match = re.search(r"\b(\d+)\s+FR\s+(\d+)\b", text, flags=re.IGNORECASE)
    if not match:
        return "", ""
    return match.group(1), match.group(2)


def classify_event(action: Any, has_actual_final_event: bool) -> dict[str, str]:
    label = clean(action)
    lower = label.lower()
    if not lower:
        return {
            "event_class": "excluded",
            "exclusion_reason": "missing_action_label",
            "parser_confidence": "low",
            "parser_notes": "No timetable action label.",
        }

    def out(event_class: str, reason: str, confidence: str, note: str) -> dict[str, str]:
        return {
            "event_class": event_class,
            "exclusion_reason": reason,
            "parser_confidence": confidence,
            "parser_notes": note,
        }

    if re.search(r"\b(anprm|nprm|proposed rule|proposal|proposed revision|supplemental nprm)\b", lower):
        return out("excluded", "not_final_proposed_or_prerule_action", "high", "Proposed/prerule action label.")
    if re.search(r"comment period|reopen|reopening", lower):
        return out("excluded", "not_final_comment_period_action", "high", "Comment-period action label.")
    if re.search(r"correction|correcting|technical amendment|technical correction|amendment correction", lower):
        return out("excluded", "not_primary_correction_or_technical", "high", "Correction or technical-amendment label.")
    if re.search(r"briefing package", lower):
        return out("excluded", "not_primary_internal_process_milestone", "high", "Internal process milestone.")
    if re.search(r"confirmation", lower):
        return out("excluded", "not_primary_confirmation_or_support_action", "high", "Confirmation/support action label.")
    if re.search(r"effective|compliance date", lower):
        return out("excluded", "not_primary_effective_or_compliance_date", "high", "Effective-date or compliance-date event.")
    if re.search(r"delay|delayed|stay|suspension|suspend|postpone|extension of effective|extend effective", lower):
        return out("excluded", "not_primary_delay_stay_or_extension", "high", "Delay, stay, or extension label.")
    if re.search(r"withdraw|withdrawn|withdrawal|deleted|removed|rescission", lower):
        return out("excluded", "not_primary_withdrawal_or_rescission", "high", "Withdrawal, deletion, or rescission label.")
    if "interim final" in lower:
        return out("uncertain", "interim_final_rule_not_primary_strict", "medium", "Interim final rule kept outside strict base.")
    if "temporary final" in lower or lower.startswith("temporary rule"):
        return out("uncertain", "temporary_final_rule_not_primary_strict", "medium", "Temporary final rule kept outside strict base.")
    if "notice" in lower and not re.search(r"final (rule|action)", lower):
        return out("excluded", "not_final_notice_action", "high", "Notice action label.")

    direct_final = "direct final rule" in lower
    if direct_final:
        return out("strict_final", "", "high", "Direct Final Rule treated as a final-rule action.")

    strict_patterns = [
        r"\bfinal action\b",
        r"\bfinal rule\b",
        r"\bfinal revision\b",
        r"\bfinal regulation\b",
        r"\bfinal regulations\b",
    ]
    if any(re.search(pattern, lower) for pattern in strict_patterns):
        return out("strict_final", "", "high", "Strict final action/rule label.")

    if re.search(r"\bfinal\b", lower):
        return out(
            "uncertain",
            "uncertain_generic_final_label",
            "medium",
            "Contains 'final' but not a strict final action/rule label.",
        )
    return out("excluded", "not_final_action_label", "high", "No final-action signal in label.")


def row_has_actual_final_event(events: list[dict[str, str]]) -> bool:
    for event in events:
        label = clean(event.get("action")).lower()
        if "effective" in label or "interim final" in label:
            continue
        if re.search(r"\bfinal action\b|\bfinal rule\b|\bdirect final rule\b|\bfinal revision\b", label):
            if not re.search(r"correction|technical|delay|stay|withdraw|rescission|comment period|nprm|anprm|proposed", label):
                return True
    return False


def build_event_rows(ua: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    event_rows: list[dict[str, Any]] = []
    no_event_rows: list[dict[str, Any]] = []

    econ = ua[ua["ua_priority_economic_prong"]].copy()
    for source_index, row in econ.sort_values(["rin_norm", "ua_vintage", "ua_record_uid"]).iterrows():
        events, timetable_error = parse_timetable_json(row.get("ua_timetable_json"))
        if not events:
            base = source_context(row, source_index)
            base.update(
                {
                    "final_action_label": "",
                    "final_action_date_raw": "",
                    "final_action_date_parsed": "",
                    "final_action_year": pd.NA,
                    "final_action_fr_citation_raw": "",
                    "final_action_fr_volume": "",
                    "final_action_fr_page": "",
                    "final_action_document_number_if_available": "",
                    "parser_confidence": "low",
                    "parser_notes": timetable_error,
                    "event_class": "excluded",
                    "exclusion_reason": timetable_error or "no_timetable_events",
                }
            )
            no_event_rows.append(base)
            continue

        has_actual_final = row_has_actual_final_event(events)
        for event_index, event in enumerate(events):
            date_info = parse_ua_date(event.get("date"))
            volume, page = parse_fr_citation(event.get("fr_citation"))
            classified = classify_event(event.get("action"), has_actual_final)
            base = source_context(row, source_index)
            notes = [classified["parser_notes"]]
            if date_info["date_note"]:
                notes.append(date_info["date_note"])
            if classified["event_class"] == "strict_final" and not volume:
                notes.append("missing_fr_citation")
            base.update(
                {
                    "source_event_index": event_index,
                    "final_action_label": clean(event.get("action")),
                    "final_action_label_norm": normalize_event_label(event.get("action")),
                    "final_action_date_raw": clean(event.get("date")),
                    "final_action_date_parsed": date_info["date_parsed"],
                    "final_action_year": date_info["year"],
                    "final_action_date_granularity": date_info["granularity"],
                    "final_action_fr_citation_raw": clean(event.get("fr_citation")),
                    "final_action_fr_volume": volume,
                    "final_action_fr_page": page,
                    "final_action_document_number_if_available": "",
                    "parser_confidence": classified["parser_confidence"],
                    "parser_notes": " | ".join(note for note in notes if note),
                    "event_class": classified["event_class"],
                    "exclusion_reason": classified["exclusion_reason"],
                }
            )
            event_rows.append(base)

    events_df = pd.DataFrame(event_rows)
    no_events_df = pd.DataFrame(no_event_rows)
    return events_df, no_events_df


def source_context(row: pd.Series, source_index: int) -> dict[str, Any]:
    priority = clean(row.get("ua_priority_category"))
    return {
        "source_index": source_index,
        "source_ua_record_uid": clean(row.get("ua_record_uid")),
        "rin_norm": clean(row.get("rin_norm")).upper(),
        "ua_priority_category": priority,
        "ua_priority_economically_significant_legacy": priority == ECON_LEGACY,
        "ua_priority_section_3f1": priority == ECON_3F1,
        "ua_priority_economic_prong": priority in ECON_PRIORITY_VALUES,
        "ua_rule_title": clean(row.get("ua_rule_title")),
        "ua_agency_name": clean(row.get("ua_agency_name")),
        "ua_parent_agency_name": clean(row.get("ua_parent_agency_name")),
        "ua_rule_stage": clean(row.get("ua_rule_stage")),
        "ua_vintage": clean(row.get("ua_vintage")),
        "ua_vintage_date": clean(row.get("ua_vintage_date")),
        "ua_timetable_source_text": clean(row.get("ua_timetable_summary")),
        "ua_final_rule_dates": clean(row.get("ua_final_rule_dates")),
    }


def normalize_event_label(value: Any) -> str:
    lower = clean(value).lower()
    if "direct final rule" in lower:
        return "direct_final_rule"
    if "effective" in lower and "final action" in lower:
        return "final_action_effective"
    if "effective" in lower and "final rule" in lower:
        return "final_rule_effective"
    if "final action" in lower:
        return "final_action"
    if "final rule" in lower:
        return "final_rule"
    if "final revision" in lower:
        return "final_revision"
    return re.sub(r"[^a-z0-9]+", "_", lower).strip("_")


def classify_main_eligibility(events: pd.DataFrame) -> pd.DataFrame:
    events = events.copy()
    year_num = pd.to_numeric(events["final_action_year"], errors="coerce")
    events["stage_is_final_or_completed"] = events["ua_rule_stage"].isin(FINAL_OR_COMPLETED_STAGES)
    events["date_year_in_scope"] = year_num.ge(START_YEAR) & year_num.le(END_YEAR)
    events["is_strict_ua_core_final_action"] = (
        events["stage_is_final_or_completed"]
        & events["date_year_in_scope"]
        & events["event_class"].isin({"strict_final"})
    )

    reasons: list[str] = []
    for row in events.itertuples(index=False):
        reason = clean(getattr(row, "exclusion_reason", ""))
        if getattr(row, "is_strict_ua_core_final_action"):
            reasons.append("")
        elif not getattr(row, "stage_is_final_or_completed"):
            reasons.append("stage_not_final_or_completed")
        elif pd.isna(getattr(row, "final_action_year")):
            reasons.append("no_parseable_final_action_year")
        elif not getattr(row, "date_year_in_scope"):
            reasons.append("final_action_year_outside_2000_2024")
        elif reason:
            reasons.append(reason)
        else:
            reasons.append("not_clean_strict_final_action_candidate")
    events["exclusion_reason"] = reasons
    return events


def confidence_min(values: pd.Series) -> str:
    rank = {"high": 3, "medium": 2, "low": 1}
    texts = [clean(v).lower() for v in values if clean(v)]
    if not texts:
        return ""
    return min(texts, key=lambda item: rank.get(item, 0))


def collapse_main_events(main_events: pd.DataFrame) -> pd.DataFrame:
    if main_events.empty:
        return pd.DataFrame(columns=BASE_COLUMNS)

    main_events = main_events.copy()
    main_events["event_collapse_key"] = (
        main_events["rin_norm"].astype(str)
        + "__"
        + main_events["final_action_label_norm"].astype(str)
        + "__"
        + main_events["final_action_date_raw"].astype(str)
    )

    rows: list[dict[str, Any]] = []
    for _, grp in main_events.sort_values(
        ["rin_norm", "final_action_year", "final_action_date_raw", "ua_vintage", "final_action_label"]
    ).groupby("event_collapse_key", sort=False):
        fr_volume = pipe_join(grp["final_action_fr_volume"])
        fr_page = pipe_join(grp["final_action_fr_page"])
        parsed_dates = [clean(v) for v in grp["final_action_date_parsed"] if clean(v)]
        out = {
            "rin_norm": clean(grp.iloc[0]["rin_norm"]),
            "ua_priority_category": pipe_join(grp["ua_priority_category"]),
            "ua_priority_economically_significant_legacy": bool(grp["ua_priority_economically_significant_legacy"].any()),
            "ua_priority_section_3f1": bool(grp["ua_priority_section_3f1"].any()),
            "ua_priority_economic_prong": True,
            "ua_rule_title": pipe_join(grp["ua_rule_title"]),
            "ua_agency_name": pipe_join(grp["ua_agency_name"]),
            "ua_parent_agency_name": pipe_join(grp["ua_parent_agency_name"]),
            "ua_rule_stage": pipe_join(grp["ua_rule_stage"]),
            "ua_vintage": clean(grp["ua_vintage"].min()),
            "final_action_label": pipe_join(grp["final_action_label"]),
            "final_action_date_raw": clean(grp.iloc[0]["final_action_date_raw"]),
            "final_action_date_parsed": parsed_dates[0] if parsed_dates else "",
            "final_action_year": int(pd.to_numeric(grp["final_action_year"], errors="coerce").dropna().iloc[0]),
            "final_action_fr_citation_raw": pipe_join(grp["final_action_fr_citation_raw"]),
            "final_action_fr_volume": fr_volume,
            "final_action_fr_page": fr_page,
            "final_action_document_number_if_available": "",
            "ua_timetable_source_text": pipe_join(grp["ua_timetable_source_text"]),
            "parser_confidence": confidence_min(grp["parser_confidence"]),
            "parser_notes": pipe_join(grp["parser_notes"]),
            "source_row_count_collapsed": int(grp["source_ua_record_uid"].nunique()),
            "source_vintages_collapsed": pipe_join(grp["ua_vintage"]),
        }
        rows.append(out)

    base = pd.DataFrame(rows)
    base = base.sort_values(["final_action_year", "final_action_date_raw", "rin_norm", "final_action_label"]).reset_index(
        drop=True
    )
    base.insert(0, "ua_base_id", [f"UA-ECON-FINAL-{i:06d}" for i in range(1, len(base) + 1)])
    return base[BASE_COLUMNS]


def build_uncertain_or_excluded(events: pd.DataFrame, no_events: pd.DataFrame) -> pd.DataFrame:
    excluded = events[~events["is_strict_ua_core_final_action"]].copy()
    if not no_events.empty:
        no_events = no_events.copy()
        for col in excluded.columns:
            if col not in no_events.columns:
                no_events[col] = ""
        excluded = pd.concat([excluded, no_events[excluded.columns]], ignore_index=True)

    cols = [
        "rin_norm",
        "ua_priority_category",
        "ua_priority_economically_significant_legacy",
        "ua_priority_section_3f1",
        "ua_rule_title",
        "ua_agency_name",
        "ua_parent_agency_name",
        "ua_rule_stage",
        "ua_vintage",
        "final_action_label",
        "final_action_date_raw",
        "final_action_date_parsed",
        "final_action_year",
        "final_action_date_granularity",
        "final_action_fr_citation_raw",
        "ua_timetable_source_text",
        "event_class",
        "exclusion_reason",
        "parser_confidence",
        "parser_notes",
        "source_ua_record_uid",
    ]
    available = [col for col in cols if col in excluded.columns]
    return excluded.sort_values(["rin_norm", "ua_vintage", "final_action_date_raw", "final_action_label"])[available]


def count_by(series: pd.Series, limit: int | None = None) -> dict[str, int]:
    values = {str(k): int(v) for k, v in series.fillna("<NA>").astype(str).value_counts().to_dict().items()}
    if limit is None:
        return values
    return dict(list(values.items())[:limit])


def build_profile(
    ua: pd.DataFrame,
    events: pd.DataFrame,
    base: pd.DataFrame,
    uncertain: pd.DataFrame,
) -> dict[str, Any]:
    explicit_fr = base["final_action_fr_citation_raw"].fillna("").astype(str).str.strip().ne("")
    exact_date = base["final_action_date_parsed"].fillna("").astype(str).str.strip().ne("")
    event_counts_by_source = (
        events[events["is_strict_ua_core_final_action"]]
        .groupby("source_ua_record_uid")
        .size()
        .reset_index(name="n")
    )
    ambiguous_source_rows = int(event_counts_by_source["n"].gt(1).sum())
    excluded_reasons = count_by(uncertain["exclusion_reason"]) if "exclusion_reason" in uncertain.columns else {}

    priority_counts: dict[str, int] = {}
    for label in [ECON_LEGACY, ECON_3F1]:
        priority_counts[label] = int(base["ua_priority_category"].fillna("").str.contains(re.escape(label)).sum())

    profile = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source_file": str(UA_SOURCE.relative_to(PROJECT_ROOT)),
        "total_ua_rows_read": int(len(ua)),
        "total_distinct_rins_read": int(ua["rin_norm"].nunique()),
        "ua_rows_legacy_economically_significant": int(ua["ua_priority_economically_significant_legacy"].sum()),
        "ua_rows_section_3f1_significant": int(ua["ua_priority_section_3f1"].sum()),
        "ua_rows_economic_prong": int(ua["ua_priority_economic_prong"].sum()),
        "strict_base_rows_final_action_candidates_2000_2024": int(len(base)),
        "strict_base_distinct_rins": int(base["rin_norm"].nunique()) if not base.empty else 0,
        "source_event_rows_strict_before_vintage_collapse": int(events["is_strict_ua_core_final_action"].sum()),
        "number_with_explicit_fr_citation": int(explicit_fr.sum()),
        "number_with_parsed_final_action_date_exact_day": int(exact_date.sum()),
        "number_with_ambiguous_multiple_final_action_events": ambiguous_source_rows,
        "number_excluded_or_uncertain_event_rows": int(len(uncertain)),
        "excluded_by_reason": excluded_reasons,
        "counts_by_year": count_by(base["final_action_year"]) if not base.empty else {},
        "counts_by_agency": count_by(base["ua_agency_name"], limit=100) if not base.empty else {},
        "counts_by_priority_label": priority_counts,
        "counts_by_stage": count_by(base["ua_rule_stage"]) if not base.empty else {},
        "source_priority_counts_all_ua": count_by(ua["ua_priority_category"]),
        "source_stage_counts_all_ua": count_by(ua["ua_rule_stage"]),
        "parser_uses": "ua_timetable_json event list; ua_timetable_summary retained for source text.",
    }
    return profile


def markdown_table(df: pd.DataFrame, columns: list[str], max_rows: int) -> str:
    if df.empty:
        return "_None._"
    use = df[columns].head(max_rows).copy()
    for col in use.columns:
        use[col] = use[col].map(lambda v: clean(v)[:180])
    header = "| " + " | ".join(use.columns) + " |"
    sep = "| " + " | ".join(["---"] * len(use.columns)) + " |"
    rows = [header, sep]
    for _, row in use.iterrows():
        rows.append("| " + " | ".join(clean(row[col]).replace("|", "/") for col in use.columns) + " |")
    return "\n".join(rows)


def write_build_summary(base: pd.DataFrame, uncertain: pd.DataFrame, profile: dict[str, Any]) -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    examples = base.sort_values(["final_action_year", "rin_norm"]).head(40)
    section_3f1 = base[base["ua_priority_section_3f1"]].sort_values(["final_action_year", "rin_norm"]).head(20)
    section_3f1_years = (
        section_3f1_counts(base)
        if not base.empty
        else pd.DataFrame(columns=["final_action_year", "section_3f1_row_count"])
    )
    lines = [
        "# UA Core Step 1 Build Summary",
        "",
        "This step builds only the Unified Agenda side of the conservative economic-prong final-action base. "
        "It does not match to Federal Register documents and does not build the final FR-document dataset.",
        "",
        "## Source",
        "",
        f"- UA source: `{profile['source_file']}`",
        "- Timetable source: embedded `ua_timetable_json` action/date/FR-citation lists.",
        "- No separate more-granular UA timetable source file was present under `source_inputs/`.",
        "",
        "## Counts",
        "",
        f"- Total UA rows read: {profile['total_ua_rows_read']:,}",
        f"- Distinct RINs read: {profile['total_distinct_rins_read']:,}",
        f"- Legacy `Economically Significant` rows: {profile['ua_rows_legacy_economically_significant']:,}",
        f"- `Section 3(f)(1) Significant` rows: {profile['ua_rows_section_3f1_significant']:,}",
        f"- Strict UA-core final-action candidates, 2000-2024: {profile['strict_base_rows_final_action_candidates_2000_2024']:,}",
        f"- Distinct RINs in strict base: {profile['strict_base_distinct_rins']:,}",
        f"- Strict base rows with explicit FR citation: {profile['number_with_explicit_fr_citation']:,}",
        f"- Strict base rows with exact day-level parsed dates: {profile['number_with_parsed_final_action_date_exact_day']:,}",
        "",
        "## Parser Rules",
        "",
        "- Main inclusion requires the economic-prong priority label, `Final Rule Stage` or `Completed Actions`, "
        "a strict final-action/final-rule timetable label, and a final-action year from 2000 through 2024.",
        "- Strict labels include `Final Action`, `Final Rule`, `Final Revision`, `Final Regulation(s)`, and `Direct Final Rule`.",
        "- Effective-date and compliance-date labels are audit-only and are not included in the strict base.",
        "- NPRM/ANPRM/proposed actions, notices, corrections, technical amendments, delays, stays, withdrawals, comment-period events, "
        "interim final rules, and temporary final rules stay out of the strict base and go to the excluded/uncertain table.",
        "- Partial dates such as `08/00/2024` are used only for the year window; `final_action_date_parsed` is filled only for exact day-level dates.",
        "",
        "## Counts By Year",
        "",
        markdown_table(
            pd.DataFrame(list(profile["counts_by_year"].items()), columns=["final_action_year", "count"]).sort_values(
                "final_action_year"
            ),
            ["final_action_year", "count"],
            40,
        ),
        "",
        "## Counts By Priority Label",
        "",
        markdown_table(
            pd.DataFrame(list(profile["counts_by_priority_label"].items()), columns=["priority_label", "count"]),
            ["priority_label", "count"],
            10,
        ),
        "",
        "## Section 3(f)(1) Examples",
        "",
        "Section 3(f)(1) rows are included for Tony review because EO 14094 changed the label during 2023-2024. "
        "Rows can still have earlier final-action dates when a later UA vintage carries older timetable history.",
        "",
        markdown_table(section_3f1_years, ["final_action_year", "section_3f1_row_count"], 30),
        "",
        markdown_table(
            section_3f1,
            ["rin_norm", "final_action_year", "ua_priority_category", "ua_rule_title", "final_action_label", "final_action_date_raw"],
            20,
        ),
        "",
        "## Included Examples",
        "",
        markdown_table(
            examples,
            ["ua_base_id", "rin_norm", "final_action_year", "ua_priority_category", "ua_rule_title", "final_action_label", "final_action_fr_citation_raw"],
            40,
        ),
        "",
        "## Main Limitations",
        "",
        "- This is a UA-side event base, not a Federal Register document dataset.",
        "- The parser is intentionally conservative; generic or ambiguous labels containing `final` are audited rather than included.",
        "- A RIN can appear more than once when the UA timetable has multiple distinct final-action dates.",
        "- FR document numbers are not available in the packaged UA timetable JSON and are left blank.",
    ]
    (DOCS_DIR / "UA_CORE_STEP1_BUILD_SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def section_3f1_counts(base: pd.DataFrame) -> pd.DataFrame:
    section = base[base["ua_priority_section_3f1"]].copy()
    if section.empty:
        return pd.DataFrame(columns=["final_action_year", "section_3f1_row_count"])
    return (
        section.groupby("final_action_year", dropna=False)
        .size()
        .reset_index(name="section_3f1_row_count")
        .sort_values("final_action_year")
    )


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ua = pd.read_csv(UA_SOURCE, dtype=str, low_memory=False).fillna("")
    ua["ua_priority_economically_significant_legacy"] = ua["ua_priority_category"].eq(ECON_LEGACY)
    ua["ua_priority_section_3f1"] = ua["ua_priority_category"].eq(ECON_3F1)
    ua["ua_priority_economic_prong"] = ua["ua_priority_category"].isin(ECON_PRIORITY_VALUES)
    ua["rin_norm"] = ua["rin_norm"].map(lambda v: clean(v).upper())

    events, no_events = build_event_rows(ua)
    events = classify_main_eligibility(events)
    base = collapse_main_events(events[events["is_strict_ua_core_final_action"]].copy())
    uncertain = build_uncertain_or_excluded(events, no_events)
    profile = build_profile(ua, events, base, uncertain)

    base.to_csv(OUTPUT_DIR / "ua_econ_final_actions_base_2000_2024.csv", index=False)
    uncertain.to_csv(OUTPUT_DIR / "ua_econ_final_actions_uncertain_or_excluded_2000_2024.csv", index=False)
    (OUTPUT_DIR / "ua_econ_final_actions_profile.json").write_text(
        json.dumps(profile, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_build_summary(base, uncertain, profile)

    print(f"Wrote {len(base):,} strict UA-core final-action candidates to {OUTPUT_DIR}")
    print(f"Wrote {len(uncertain):,} uncertain/excluded event rows to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
