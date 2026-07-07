#!/usr/bin/env python3
"""Audit the UA-core economically significant final-action base."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_INPUTS = PROJECT_ROOT / "source_inputs"
OUTPUT_DIR = PROJECT_ROOT / "generated_outputs" / "ua_core_rebuild_step1"
DOCS_DIR = PROJECT_ROOT / "docs"

BASE_PATH = OUTPUT_DIR / "ua_econ_final_actions_base_2000_2024.csv"
UNCERTAIN_PATH = OUTPUT_DIR / "ua_econ_final_actions_uncertain_or_excluded_2000_2024.csv"
PROFILE_PATH = OUTPUT_DIR / "ua_econ_final_actions_profile.json"
UA_SOURCE = SOURCE_INPUTS / "ua_all_flat_rin_norm.csv.gz"
REGSTATS_COUNTS = SOURCE_INPUTS / "econ_significant_rules_by_presidential_year.csv"
STRICT_LINKED = SOURCE_INPUTS / "econ_sig_final_rules_STRICT_FR_RULE_2000_forward_linked_full.csv"

ECON_LEGACY = "Economically Significant"
ECON_3F1 = "Section 3(f)(1) Significant"
ECON_PRIORITY_VALUES = {ECON_LEGACY, ECON_3F1}
EXCLUDED_LABEL_RE = re.compile(
    r"correction|technical|delay|stay|withdraw|rescission|nprm|anprm|proposed|comment period|interim final|temporary",
    flags=re.IGNORECASE,
)
RIN_RE = re.compile(r"\b\d{4}-[A-Z0-9]{2}\d{2}\b")


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


def split_rins(value: Any) -> list[str]:
    return sorted(set(RIN_RE.findall(clean(value).upper())))


def read_csv_if_exists(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, dtype=str, low_memory=False).fillna("")


def issue(
    issue_type: str,
    severity: str = "review",
    rin_norm: str = "",
    final_action_year: Any = "",
    final_action_date_raw: Any = "",
    final_action_label: Any = "",
    ua_priority_category: Any = "",
    ua_rule_title: Any = "",
    ua_agency_name: Any = "",
    details: str = "",
    source_file: str = "",
    comparison_value: Any = "",
) -> dict[str, Any]:
    return {
        "issue_type": issue_type,
        "severity": severity,
        "rin_norm": clean(rin_norm),
        "final_action_year": clean(final_action_year),
        "final_action_date_raw": clean(final_action_date_raw),
        "final_action_label": clean(final_action_label),
        "ua_priority_category": clean(ua_priority_category),
        "ua_rule_title": clean(ua_rule_title),
        "ua_agency_name": clean(ua_agency_name),
        "details": clean(details),
        "source_file": clean(source_file),
        "comparison_value": clean(comparison_value),
    }


def base_issue_from_row(issue_type: str, row: pd.Series, details: str, severity: str = "review") -> dict[str, Any]:
    return issue(
        issue_type=issue_type,
        severity=severity,
        rin_norm=row.get("rin_norm", ""),
        final_action_year=row.get("final_action_year", ""),
        final_action_date_raw=row.get("final_action_date_raw", ""),
        final_action_label=row.get("final_action_label", ""),
        ua_priority_category=row.get("ua_priority_category", ""),
        ua_rule_title=row.get("ua_rule_title", ""),
        ua_agency_name=row.get("ua_agency_name", ""),
        details=details,
        source_file=str(BASE_PATH.relative_to(PROJECT_ROOT)),
    )


def extract_rins_from_frame(df: pd.DataFrame) -> set[str]:
    if df.empty:
        return set()
    likely_cols = [
        col
        for col in df.columns
        if any(token in col.lower() for token in ["rin", "matched_econ_rin_list", "candidate_econ_rin_list"])
    ]
    rins: set[str] = set()
    for col in likely_cols:
        for value in df[col].dropna().astype(str):
            rins.update(split_rins(value))
    return rins


def year_counts_from_frame(df: pd.DataFrame) -> tuple[str, pd.Series]:
    if df.empty:
        return "", pd.Series(dtype=int)
    for col in ["final_action_year", "fr_issue_date", "fr_publication_date", "publication_date", "presidential_year"]:
        if col in df.columns:
            if col.endswith("_date") or col in {"fr_issue_date", "publication_date"}:
                years = pd.to_datetime(df[col], errors="coerce").dt.year
                return "calendar_year", years.dropna().astype(int).value_counts().sort_index()
            years = pd.to_numeric(df[col], errors="coerce")
            return col, years.dropna().astype(int).value_counts().sort_index()
    return "", pd.Series(dtype=int)


def add_internal_issues(base: pd.DataFrame, uncertain: pd.DataFrame, ua: pd.DataFrame) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []

    dup_cols = ["rin_norm", "final_action_date_raw", "final_action_label"]
    if not base.empty:
        duplicates = base[base.duplicated(dup_cols, keep=False)].sort_values(dup_cols)
        for _, row in duplicates.iterrows():
            issues.append(base_issue_from_row("duplicate_rin_date_final_action_combination", row, "Duplicate strict base key."))

        multi_dates = base.groupby("rin_norm")["final_action_date_raw"].nunique()
        for rin in multi_dates[multi_dates > 1].index:
            rows = base[base["rin_norm"].eq(rin)]
            issues.append(
                issue(
                    "same_rin_multiple_final_action_dates",
                    rin_norm=rin,
                    details=pipe_join(rows["final_action_date_raw"]),
                    comparison_value=int(multi_dates.loc[rin]),
                )
            )

        for _, row in base[base["final_action_label"].str.contains(EXCLUDED_LABEL_RE, na=False)].iterrows():
            issues.append(base_issue_from_row("included_label_has_excluded_term", row, "Strict base label matches excluded-term regex.", "high"))

        for _, row in base[base["final_action_fr_citation_raw"].fillna("").str.strip().eq("")].iterrows():
            issues.append(base_issue_from_row("missing_fr_citation_in_strict_base", row, "UA timetable event lacks an FR citation."))

        missing_title_agency = base[
            base["ua_rule_title"].fillna("").str.strip().eq("")
            | base["ua_agency_name"].fillna("").str.strip().eq("")
        ]
        for _, row in missing_title_agency.iterrows():
            issues.append(base_issue_from_row("missing_title_or_agency", row, "Missing title or agency in strict base.", "high"))

        partial_date = base[
            base["final_action_date_parsed"].fillna("").str.strip().eq("")
            | base["parser_notes"].fillna("").str.contains("month_year|year_only|unstructured_year", regex=True)
        ]
        for _, row in partial_date.iterrows():
            issues.append(base_issue_from_row("partial_or_non_exact_final_action_date", row, row.get("parser_notes", "")))

        section_pre_2023 = base[
            base["ua_priority_section_3f1"].astype(str).str.lower().isin(["true", "1"])
            & pd.to_numeric(base["final_action_year"], errors="coerce").lt(2023)
        ]
        for _, row in section_pre_2023.iterrows():
            issues.append(
                base_issue_from_row(
                    "section_3f1_priority_on_pre_2023_final_action_year",
                    row,
                    "Later UA vintages may carry Section 3(f)(1) priority while retaining older timetable history.",
                )
            )

    if not uncertain.empty:
        outside = uncertain[uncertain["exclusion_reason"].eq("final_action_year_outside_2000_2024")]
        for _, row in outside.iterrows():
            issues.append(
                issue(
                    "final_action_date_outside_2000_2024",
                    rin_norm=row.get("rin_norm", ""),
                    final_action_year=row.get("final_action_year", ""),
                    final_action_date_raw=row.get("final_action_date_raw", ""),
                    final_action_label=row.get("final_action_label", ""),
                    ua_priority_category=row.get("ua_priority_category", ""),
                    ua_rule_title=row.get("ua_rule_title", ""),
                    ua_agency_name=row.get("ua_agency_name", ""),
                    details=row.get("parser_notes", ""),
                    source_file=str(UNCERTAIN_PATH.relative_to(PROJECT_ROOT)),
                )
            )

        failed = uncertain[
            uncertain["exclusion_reason"].isin(["no_parseable_final_action_year", "unparseable_timetable_json"])
            | uncertain["parser_notes"].fillna("").str.contains("unparseable|invalid", regex=True)
        ]
        for _, row in failed.iterrows():
            issues.append(
                issue(
                    "unparseable_timetable_or_date",
                    rin_norm=row.get("rin_norm", ""),
                    final_action_year=row.get("final_action_year", ""),
                    final_action_date_raw=row.get("final_action_date_raw", ""),
                    final_action_label=row.get("final_action_label", ""),
                    ua_priority_category=row.get("ua_priority_category", ""),
                    ua_rule_title=row.get("ua_rule_title", ""),
                    ua_agency_name=row.get("ua_agency_name", ""),
                    details=f"{row.get('exclusion_reason', '')}: {row.get('parser_notes', '')}",
                    source_file=str(UNCERTAIN_PATH.relative_to(PROJECT_ROOT)),
                )
            )

    ua_econ = ua[ua["ua_priority_category"].isin(ECON_PRIORITY_VALUES)].copy()
    base_rins = set(base["rin_norm"]) if not base.empty else set()
    for rin, grp in ua_econ.groupby("rin_norm"):
        if rin not in base_rins:
            first = grp.sort_values("ua_vintage").iloc[0]
            issues.append(
                issue(
                    "econ_prong_rin_has_no_strict_base_final_action",
                    rin_norm=rin,
                    ua_priority_category=pipe_join(grp["ua_priority_category"]),
                    ua_rule_title=first.get("ua_rule_title", ""),
                    ua_agency_name=first.get("ua_agency_name", ""),
                    details=f"Stages: {pipe_join(grp['ua_rule_stage'])}; vintages: {pipe_join(grp['ua_vintage'])}",
                    source_file=str(UA_SOURCE.relative_to(PROJECT_ROOT)),
                    comparison_value=len(grp),
                )
            )

    priority_by_rin = ua.groupby("rin_norm")["ua_priority_category"].agg(lambda s: sorted(set(clean(v) for v in s if clean(v))))
    for rin, labels in priority_by_rin.items():
        has_legacy = ECON_LEGACY in labels
        has_3f1 = ECON_3F1 in labels
        has_non_econ = any(label not in ECON_PRIORITY_VALUES for label in labels)
        if has_legacy and has_non_econ:
            issues.append(
                issue(
                    "same_rin_legacy_econ_and_non_econ_priority_across_vintages",
                    rin_norm=rin,
                    details=pipe_join(labels),
                    source_file=str(UA_SOURCE.relative_to(PROJECT_ROOT)),
                )
            )
        if has_legacy and has_3f1:
            issues.append(
                issue(
                    "same_rin_legacy_econ_and_section_3f1_priority_across_vintages",
                    rin_norm=rin,
                    details=pipe_join(labels),
                    source_file=str(UA_SOURCE.relative_to(PROJECT_ROOT)),
                )
            )
    return issues


def candidate_baseline_paths() -> list[Path]:
    explicit = [
        PROJECT_ROOT / "data/release_current/econ_sig_final_rule_document_candidates_2000_2024.csv",
        PROJECT_ROOT / "data/release_current/econ_sig_final_rules_rule_level_2000_2024.csv",
        PROJECT_ROOT / "data/release_current/econ_sig_final_rules_rule_level_2000_2024_cfr_audited.csv",
        PROJECT_ROOT
        / "generated_outputs/rebuilt_from_packaged_inputs/econ_sig_final_rule_universe_v2/econ_sig_final_rule_document_candidates_2000_2024.csv",
        PROJECT_ROOT
        / "generated_outputs/rebuilt_from_packaged_inputs/econ_sig_final_rule_universe_v2/econ_sig_final_rules_rule_level_2000_2024.csv",
        PROJECT_ROOT
        / "generated_outputs/rebuilt_from_packaged_inputs/econ_sig_final_rule_universe_v2/econ_sig_final_rules_rule_level_2000_2024_cfr_audited.csv",
        REGSTATS_COUNTS,
        STRICT_LINKED,
    ]
    discovered = sorted(PROJECT_ROOT.rglob("ua_fr_econ_sig_primary_substantive_final_rules_2000_forward.csv"))
    seen: set[Path] = set()
    out: list[Path] = []
    for path in explicit + discovered:
        if path.exists() and path not in seen:
            seen.add(path)
            out.append(path)
    return out


def add_baseline_comparisons(base: pd.DataFrame) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    issues: list[dict[str, Any]] = []
    base_rins = set(base["rin_norm"]) if not base.empty else set()

    rows.append(
        {
            "comparison": "new_ua_core_base",
            "year_type": "calendar_year",
            "year": "ALL",
            "count": int(len(base)),
            "notes": "Strict UA-core final-action candidates; not FR documents.",
        }
    )
    if not base.empty:
        for year, count in base["final_action_year"].value_counts().sort_index().items():
            rows.append(
                {
                    "comparison": "new_ua_core_base",
                    "year_type": "calendar_year",
                    "year": int(year),
                    "count": int(count),
                    "notes": "Strict UA-core final-action candidates; not FR documents.",
                }
            )

    for path in candidate_baseline_paths():
        df = read_csv_if_exists(path)
        rel = str(path.relative_to(PROJECT_ROOT))
        if df.empty:
            continue
        rins = extract_rins_from_frame(df)
        missing = sorted(rins - base_rins)
        present = sorted(rins & base_rins)
        rows.append(
            {
                "comparison": rel,
                "year_type": "all_rows_or_records",
                "year": "ALL",
                "count": int(len(df)),
                "notes": f"Baseline only; distinct extracted RINs={len(rins)}, overlap with new base={len(present)}.",
            }
        )
        year_type, counts = year_counts_from_frame(df)
        for year, count in counts.items():
            rows.append(
                {
                    "comparison": rel,
                    "year_type": year_type,
                    "year": int(year),
                    "count": int(count),
                    "notes": "Baseline count; not authoritative for UA-core.",
                }
            )
        for rin in missing[:5000]:
            issues.append(
                issue(
                    "baseline_rin_absent_from_new_ua_core_base",
                    rin_norm=rin,
                    details="RIN appears in local comparison baseline but not strict UA-core base.",
                    source_file=rel,
                    comparison_value=f"baseline_rins={len(rins)}; overlap={len(present)}",
                )
            )

    return pd.DataFrame(rows), issues


def add_external_benchmark_issues(base: pd.DataFrame, counts: pd.DataFrame) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    base_rins = set(base["rin_norm"]) if not base.empty else set()

    strict = read_csv_if_exists(STRICT_LINKED)
    if not strict.empty:
        for col in [
            "oira_economically_significant",
            "fr_tracking_econ_significant",
            "fr_tracking_3f1_significant",
        ]:
            if col not in strict.columns:
                strict[col] = ""
        econ_mask = strict[["oira_economically_significant", "fr_tracking_econ_significant", "fr_tracking_3f1_significant"]].apply(
            lambda row: any(clean(v).lower() in {"yes", "true", "1", "1.0"} for v in row),
            axis=1,
        )
        date_col = "oira_publication_date" if "oira_publication_date" in strict.columns else "fr_publication_date"
        years = pd.to_datetime(strict[date_col], errors="coerce").dt.year
        in_scope = years.ge(2000) & years.le(2024)
        stage = strict.get("oira_stage", pd.Series("", index=strict.index)).fillna("").str.contains("Final", case=False)
        target = strict[econ_mask & in_scope & stage].copy()
        target_rins: set[str] = set()
        for col in ["rin_primary", "rin", "rin_list", "fr_rins"]:
            if col in target.columns:
                for value in target[col].astype(str):
                    target_rins.update(split_rins(value))
        for rin in sorted(target_rins - base_rins):
            issues.append(
                issue(
                    "oira_or_regstats_econ_final_rin_absent_from_new_ua_core_base",
                    rin_norm=rin,
                    details="RIN appears in local OIRA/RegStats linked economic-significance final-stage benchmark but not strict UA-core base.",
                    source_file=str(STRICT_LINKED.relative_to(PROJECT_ROOT)),
                )
            )

    regstats = read_csv_if_exists(REGSTATS_COUNTS)
    if not regstats.empty and not counts.empty:
        year_col = "Presidential Year (February 1 - January 31)"
        count_col = "Economically Significant Rules Published"
        if year_col in regstats.columns and count_col in regstats.columns:
            base_by_year = (
                counts[
                    (counts["comparison"] == "new_ua_core_base")
                    & (counts["year_type"] == "calendar_year")
                    & (counts["year"] != "ALL")
                ]
                .assign(year=lambda d: pd.to_numeric(d["year"], errors="coerce"), count=lambda d: pd.to_numeric(d["count"], errors="coerce"))
                .set_index("year")["count"]
            )
            for _, row in regstats.iterrows():
                year = pd.to_numeric(row.get(year_col), errors="coerce")
                benchmark = pd.to_numeric(row.get(count_col), errors="coerce")
                if pd.isna(year) or pd.isna(benchmark) or year < 2000 or year > 2024:
                    continue
                base_count = int(base_by_year.get(int(year), 0))
                if benchmark > 0 and base_count < 0.7 * benchmark:
                    issues.append(
                        issue(
                            "new_ua_core_count_far_below_regstats_benchmark",
                            final_action_year=int(year),
                            details=(
                                "Calendar-year UA-core count is far below RegStats presidential-year benchmark; "
                                "calendar/presidential-year definitions differ, so review rather than treat as error."
                            ),
                            source_file=str(REGSTATS_COUNTS.relative_to(PROJECT_ROOT)),
                            comparison_value=f"ua_core_calendar_count={base_count}; regstats_presidential_year_count={int(benchmark)}",
                        )
                    )
    return issues


def markdown_table(df: pd.DataFrame, columns: list[str], max_rows: int = 20) -> str:
    if df.empty:
        return "_None._"
    use = df[columns].head(max_rows).copy()
    for col in use.columns:
        use[col] = use[col].map(lambda v: clean(v)[:180])
    rows = ["| " + " | ".join(use.columns) + " |", "| " + " | ".join(["---"] * len(use.columns)) + " |"]
    for _, row in use.iterrows():
        rows.append("| " + " | ".join(clean(row[col]).replace("|", "/") for col in use.columns) + " |")
    return "\n".join(rows)


def issue_examples(issues: pd.DataFrame, issue_type: str, max_rows: int = 20) -> pd.DataFrame:
    if issues.empty:
        return issues
    return issues[issues["issue_type"].eq(issue_type)].head(max_rows)


def write_reports(base: pd.DataFrame, uncertain: pd.DataFrame, counts: pd.DataFrame, issues: pd.DataFrame, profile: dict[str, Any]) -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    report_path = OUTPUT_DIR / "ua_core_step1_audit_report.md"
    docs_path = DOCS_DIR / "UA_CORE_STEP1_AUDIT.md"

    clean_examples = base.sort_values(["final_action_year", "rin_norm"]).head(20)
    excluded_examples = uncertain.sort_values(["exclusion_reason", "rin_norm"]).head(20)
    uncertain_examples = (
        uncertain[uncertain["event_class"].eq("uncertain")].copy()
        if "event_class" in uncertain.columns
        else pd.DataFrame()
    )
    if not uncertain_examples.empty:
        uncertain_examples["issue_type"] = "uncertain_excluded_event"
        uncertain_examples["details"] = uncertain_examples["exclusion_reason"] + ": " + uncertain_examples["parser_notes"]
    ambiguous_examples = pd.concat(
        [uncertain_examples, issue_examples(issues, "same_rin_multiple_final_action_dates", 20)],
        ignore_index=True,
        sort=False,
    ).head(20)
    possible_missing = issues[
        issues["issue_type"].isin(
            [
                "econ_prong_rin_has_no_strict_base_final_action",
                "baseline_rin_absent_from_new_ua_core_base",
                "oira_or_regstats_econ_final_rin_absent_from_new_ua_core_base",
                "new_ua_core_count_far_below_regstats_benchmark",
            ]
        )
    ].head(20)
    section_3f1 = base[base["ua_priority_section_3f1"].astype(str).str.lower().isin(["true", "1"])].head(20)
    section_3f1_years = (
        base[base["ua_priority_section_3f1"].astype(str).str.lower().isin(["true", "1"])]
        .groupby("final_action_year", dropna=False)
        .size()
        .reset_index(name="section_3f1_row_count")
        .sort_values("final_action_year")
        if not base.empty
        else pd.DataFrame(columns=["final_action_year", "section_3f1_row_count"])
    )
    multiple_dates = issue_examples(issues, "same_rin_multiple_final_action_dates", 20)
    with_cites = base[base["final_action_fr_citation_raw"].fillna("").str.strip().ne("")].head(20)
    without_cites = base[base["final_action_fr_citation_raw"].fillna("").str.strip().eq("")].head(20)

    summary_lines = [
        "# UA Core Step 1 Audit",
        "",
        "This audit treats old document-level and rule-level files as comparison baselines, not truth sources.",
        "",
        "## Summary Counts",
        "",
        f"- Strict UA-core base rows: {len(base):,}",
        f"- Distinct RINs in base: {base['rin_norm'].nunique() if not base.empty else 0:,}",
        f"- Rows with explicit FR citations: {int(base['final_action_fr_citation_raw'].fillna('').str.strip().ne('').sum()) if not base.empty else 0:,}",
        f"- Uncertain/excluded event rows: {len(uncertain):,}",
        f"- Possible missing/suspicious rows written: {len(issues):,}",
        f"- Section 3(f)(1) base rows: {int(base['ua_priority_section_3f1'].astype(str).str.lower().isin(['true', '1']).sum()) if not base.empty else 0:,}",
        "",
        "## Section 3(f)(1) Years",
        "",
        "Section 3(f)(1) rows are included for review because 2023-2024 may use that label for the economic prong. "
        "Pre-2023 final-action years can appear when a 2023-2024 UA vintage carries older timetable history.",
        "",
        markdown_table(section_3f1_years, ["final_action_year", "section_3f1_row_count"], 30),
        "",
        "## Counts Table Preview",
        "",
        markdown_table(counts, ["comparison", "year_type", "year", "count", "notes"], 30),
        "",
        "## Internal Issue Counts",
        "",
        markdown_table(
            issues["issue_type"].value_counts().reset_index().rename(columns={"issue_type": "issue_type", "count": "count"}),
            ["issue_type", "count"],
            40,
        )
        if not issues.empty
        else "_None._",
        "",
        "## 20 Clean Included Records",
        "",
        markdown_table(
            clean_examples,
            ["ua_base_id", "rin_norm", "final_action_year", "ua_priority_category", "ua_rule_title", "final_action_label", "final_action_fr_citation_raw"],
            20,
        ),
        "",
        "## 20 Excluded Records With Reasons",
        "",
        markdown_table(
            excluded_examples,
            ["rin_norm", "ua_priority_category", "ua_rule_stage", "final_action_label", "final_action_date_raw", "exclusion_reason"],
            20,
        ),
        "",
        "## 20 Uncertain/Ambiguous Records",
        "",
        markdown_table(
            ambiguous_examples,
            ["issue_type", "rin_norm", "final_action_year", "final_action_date_raw", "final_action_label", "details"]
            if "issue_type" in ambiguous_examples.columns
            else ["rin_norm", "final_action_label", "final_action_date_raw", "exclusion_reason"],
            20,
        ),
        "",
        "## 20 Possible Missing Records",
        "",
        markdown_table(
            possible_missing,
            ["issue_type", "rin_norm", "ua_priority_category", "ua_rule_title", "details", "source_file", "comparison_value"],
            20,
        ),
        "",
        "## Section 3(f)(1) Examples",
        "",
        markdown_table(
            section_3f1,
            ["ua_base_id", "rin_norm", "final_action_year", "ua_rule_title", "final_action_label", "final_action_date_raw"],
            20,
        ),
        "",
        "## RINs With Multiple Final-Action Dates",
        "",
        markdown_table(multiple_dates, ["issue_type", "rin_norm", "details", "comparison_value"], 20),
        "",
        "## Examples With Explicit FR Citations",
        "",
        markdown_table(
            with_cites,
            ["ua_base_id", "rin_norm", "final_action_year", "final_action_label", "final_action_fr_citation_raw", "ua_rule_title"],
            20,
        ),
        "",
        "## Examples Without FR Citations",
        "",
        markdown_table(
            without_cites,
            ["ua_base_id", "rin_norm", "final_action_year", "final_action_label", "final_action_date_raw", "ua_rule_title"],
            20,
        ),
        "",
        "## Missingness Risks",
        "",
        "- UA timetable records are embedded JSON within a per-RIN/per-vintage flat table; no separate source timetable-row file was packaged.",
        "- Generic final labels, interim final rules, temporary final rules, notices, corrections, delays, stays, and withdrawals are audited rather than included.",
        "- Old FR-linked baselines can contain RIN aliases and document-level evidence that a pure UA-core pass intentionally has not resolved yet.",
        "- RegStats counts use presidential years and external determinations; this step uses UA final-action calendar years.",
    ]
    report_text = "\n".join(summary_lines) + "\n"
    report_path.write_text(report_text, encoding="utf-8")

    docs_lines = summary_lines[:]
    docs_path.write_text("\n".join(docs_lines) + "\n", encoding="utf-8")


def main() -> None:
    if not BASE_PATH.exists():
        raise SystemExit(f"Missing {BASE_PATH}. Run 01_build_ua_econ_final_actions.py first.")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    base = read_csv_if_exists(BASE_PATH)
    uncertain = read_csv_if_exists(UNCERTAIN_PATH)
    ua = pd.read_csv(UA_SOURCE, dtype=str, low_memory=False).fillna("")
    ua["rin_norm"] = ua["rin_norm"].map(lambda v: clean(v).upper())
    profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8")) if PROFILE_PATH.exists() else {}

    internal_issues = add_internal_issues(base, uncertain, ua)
    counts, baseline_issues = add_baseline_comparisons(base)
    benchmark_issues = add_external_benchmark_issues(base, counts)
    issues = pd.DataFrame(internal_issues + baseline_issues + benchmark_issues)
    if issues.empty:
        issues = pd.DataFrame(
            columns=[
                "issue_type",
                "severity",
                "rin_norm",
                "final_action_year",
                "final_action_date_raw",
                "final_action_label",
                "ua_priority_category",
                "ua_rule_title",
                "ua_agency_name",
                "details",
                "source_file",
                "comparison_value",
            ]
        )
    issues = issues.sort_values(["issue_type", "rin_norm", "final_action_year", "final_action_date_raw"]).reset_index(drop=True)

    counts.to_csv(OUTPUT_DIR / "ua_core_step1_audit_counts.csv", index=False)
    issues.to_csv(OUTPUT_DIR / "ua_core_step1_possible_missing_or_suspicious.csv", index=False)
    write_reports(base, uncertain, counts, issues, profile)
    print(f"Wrote audit report and {len(issues):,} possible missing/suspicious rows to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
