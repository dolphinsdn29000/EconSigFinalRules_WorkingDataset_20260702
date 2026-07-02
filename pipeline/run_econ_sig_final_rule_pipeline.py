#!/usr/bin/env python3
"""Rebuild the working economically significant final-rule dataset package.

This runner is intentionally thin.  The core universe-building logic is kept in
`build_union_universe_original_snapshot.py`, a packaged copy of the build logic used to
create the current release.  This wrapper points that script at the packaged
inputs, then writes the external economic-significance validation audit.

The resulting dataset is a working/candidate universe, not a final legal truth
table.  The methods notes in `docs/` explain why the package keeps construction
and validation evidence visibly separated.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd


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


def doc_key(date_value: Any, frdoc_value: Any) -> str:
    date_text = clean(date_value)
    frdoc = clean(frdoc_value)
    return f"{date_text}__FRDOC_{frdoc}" if date_text and frdoc else ""


def split_rins(value: Any) -> list[str]:
    return sorted(set(re.findall(r"\b\d{4}-[A-Z0-9]{2}\d{2}\b", str(value).upper())))


def yesish(value: Any) -> bool:
    return clean(value).lower() in {"yes", "true", "1", "1.0"}


def load_snapshot_module(package_root: Path):
    path = package_root / "pipeline" / "build_union_universe_original_snapshot.py"
    spec = importlib.util.spec_from_file_location("build_union_universe_original_snapshot", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not import pipeline snapshot at {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_working_universe_build(package_root: Path, output_dir: Path, year_min: int, year_max: int) -> None:
    source_inputs = package_root / "source_inputs"
    module = load_snapshot_module(package_root)

    module.ROOT = package_root
    module.OUT = output_dir
    module.MIN_PRESIDENTIAL_YEAR = year_min
    module.MAX_PRESIDENTIAL_YEAR = year_max
    module.FR_RAW = source_inputs / "fr_final_rules_rawparsed.csv.gz"
    module.FR_RIN = source_inputs / "fr_final_rules_rin_exploded.csv.gz"
    module.UA_ALL = source_inputs / "ua_all_flat_rin_norm.csv.gz"
    module.STRICT_LINKED = source_inputs / "econ_sig_final_rules_STRICT_FR_RULE_2000_forward_linked_full.csv"
    module.REGSTATS_COUNTS = source_inputs / "econ_significant_rules_by_presidential_year.csv"
    module.main()


def external_econ_flag(row: pd.Series) -> bool:
    return (
        yesish(row.get("oira_economically_significant", ""))
        or yesish(row.get("fr_tracking_econ_significant", ""))
        or yesish(row.get("fr_tracking_3f1_significant", ""))
    )


def external_major_only_flag(row: pd.Series) -> bool:
    major = yesish(row.get("oira_major", "")) or yesish(row.get("fr_tracking_major", ""))
    return bool(major and not external_econ_flag(row))


def build_external_econ_only_audit(package_root: Path, output_dir: Path) -> dict[str, int]:
    source_inputs = package_root / "source_inputs"
    audits = output_dir / "audits"
    audits.mkdir(parents=True, exist_ok=True)
    snapshot = load_snapshot_module(package_root)

    strict = pd.read_csv(
        source_inputs / "econ_sig_final_rules_STRICT_FR_RULE_2000_forward_linked_full.csv",
        dtype=str,
        low_memory=False,
    ).fillna("")
    docs = pd.read_csv(
        output_dir / "econ_sig_final_rule_document_candidates_2000_2024.csv",
        dtype=str,
        keep_default_na=False,
        low_memory=False,
    )
    ua = pd.read_csv(
        source_inputs / "ua_all_flat_rin_norm.csv.gz",
        dtype=str,
        low_memory=False,
    ).fillna("")

    strict["fr_doc_key"] = [doc_key(d, n) for d, n in zip(strict["fr_publication_date"], strict["fr_document_number"])]
    strict["action_family"] = strict["fr_action"].map(snapshot.classify_action)
    strict["external_econ_sig_only"] = strict.apply(external_econ_flag, axis=1)
    strict["external_major_only_signal"] = strict.apply(external_major_only_flag, axis=1)

    target = strict[
        strict["official_fr_type"].str.lower().eq("rule")
        & strict["external_econ_sig_only"]
        & strict["action_family"].isin(PRIMARY_ACTION_FAMILIES)
        & strict["fr_publication_date"].ge("2000-01-01")
        & strict["fr_publication_date"].le("2024-12-31")
        & strict["fr_doc_key"].ne("")
    ].copy()
    target = target.sort_values(["fr_publication_date", "fr_document_number", "source_system"]).drop_duplicates(
        "fr_doc_key", keep="first"
    )

    major_only = strict[
        strict["official_fr_type"].str.lower().eq("rule")
        & strict["external_major_only_signal"]
        & strict["action_family"].isin(PRIMARY_ACTION_FAMILIES)
        & strict["fr_publication_date"].ge("2000-01-01")
        & strict["fr_publication_date"].le("2024-12-31")
        & strict["fr_doc_key"].ne("")
    ].copy()
    major_only = major_only.drop_duplicates("fr_doc_key", keep="first")

    for col in ["source_ua_any_econ_rin", "audited_primary"]:
        docs[col] = docs[col].astype(str).str.upper().isin({"TRUE", "1", "YES"})
    docs["calendar_in_scope"] = docs["fr_issue_date"].ge("2000-01-01") & docs["fr_issue_date"].le("2024-12-31")
    ua_priority_doc_keys = set(
        docs.loc[docs["source_ua_any_econ_rin"] & docs["audited_primary"] & docs["calendar_in_scope"], "fr_doc_key"]
    )
    target["present_in_ua_priority_construction"] = target["fr_doc_key"].isin(ua_priority_doc_keys)
    missing = target[~target["present_in_ua_priority_construction"]].copy()

    ua["rin_norm"] = ua["rin_norm"].str.upper()
    ua_econ = set(ua.loc[ua["ua_priority_category"].isin(ECON_PRIORITY_VALUES), "rin_norm"])
    ua_any = set(ua["rin_norm"])

    def target_rins(row: pd.Series) -> list[str]:
        return (
            split_rins(row.get("rin_list", ""))
            or split_rins(row.get("rin_primary", ""))
            or split_rins(row.get("fr_rins", ""))
            or split_rins(row.get("rin", ""))
        )

    def miss_reason(row: pd.Series) -> str:
        rins = target_rins(row)
        if not rins:
            return "external_econ_doc_has_no_rin_in_target_record"
        if any(rin in ua_econ for rin in rins):
            return "target_rin_has_ua_econ_but_doc_not_in_ua_construction_path"
        if any(rin in ua_any for rin in rins):
            return "target_rin_in_ua_but_not_ua_econ_priority"
        return "target_rin_not_found_in_ua"

    missing["target_rins"] = missing.apply(lambda row: " | ".join(target_rins(row)), axis=1)
    missing["miss_reason"] = missing.apply(miss_reason, axis=1)

    target_cols = [
        "fr_doc_key",
        "fr_publication_date",
        "fr_document_number",
        "rin_primary",
        "rin_list",
        "source_system",
        "target_basis",
        "oira_economically_significant",
        "fr_tracking_econ_significant",
        "fr_tracking_3f1_significant",
        "oira_major",
        "fr_tracking_major",
        "fr_action",
        "fr_title",
        "present_in_ua_priority_construction",
    ]
    missing_cols = target_cols + ["target_rins", "miss_reason"]
    target[target_cols].to_csv(audits / "external_econ_only_comparison_target_2000_2024_no_major_only.csv", index=False)
    missing[missing_cols].to_csv(
        audits / "external_econ_only_missing_from_ua_priority_construction_2000_2024.csv",
        index=False,
    )
    major_only[
        [
            "fr_doc_key",
            "fr_publication_date",
            "fr_document_number",
            "rin_primary",
            "rin_list",
            "oira_economically_significant",
            "fr_tracking_econ_significant",
            "fr_tracking_3f1_significant",
            "oira_major",
            "fr_tracking_major",
            "fr_action",
            "fr_title",
        ]
    ].to_csv(audits / "external_major_only_excluded_from_comparison_2000_2024.csv", index=False)

    summary = {
        "external_econ_only_target_docs": int(len(target)),
        "present_in_ua_priority_construction": int(target["present_in_ua_priority_construction"].sum()),
        "missing_from_ua_priority_construction": int(len(missing)),
        "major_only_excluded_from_comparison": int(len(major_only)),
    }
    summary["missing_reason_counts"] = {
        str(k): int(v) for k, v in missing["miss_reason"].value_counts().to_dict().items()
    }
    (audits / "external_econ_only_validation_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def write_run_summary(package_root: Path, output_dir: Path, validation_summary: dict[str, Any]) -> None:
    rules = pd.read_csv(output_dir / "econ_sig_final_rules_rule_level_2000_2024.csv", dtype=str, keep_default_na=False)
    for col in ["source_ua_any_econ_rin", "source_regstats_oira_linked"]:
        rules[col] = rules[col].astype(str).str.upper().isin({"TRUE", "1", "YES"})
    summary = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "package_root": str(package_root),
        "output_dir": str(output_dir),
        "rule_rows": int(len(rules)),
        "cfr_audited_rule_rows": int((rules["audited_primary"].astype(str).str.upper().isin({"TRUE", "1", "YES"})).sum()),
        "source_mix": {
            "both_ua_priority_and_external": int((rules["source_ua_any_econ_rin"] & rules["source_regstats_oira_linked"]).sum()),
            "ua_priority_only": int((rules["source_ua_any_econ_rin"] & ~rules["source_regstats_oira_linked"]).sum()),
            "external_only": int((~rules["source_ua_any_econ_rin"] & rules["source_regstats_oira_linked"]).sum()),
        },
        "literal_2025_publication_rows": int(rules["representative_fr_issue_date"].str.startswith("2025-").sum()),
        "external_econ_only_validation": validation_summary,
    }
    (output_dir / "PACKAGE_RUN_SUMMARY.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")


def main() -> None:
    default_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package-root", type=Path, default=default_root)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=default_root / "generated_outputs" / "rebuilt_from_packaged_inputs" / "econ_sig_final_rule_universe_v2",
    )
    parser.add_argument("--year-min", type=int, default=2000)
    parser.add_argument("--year-max", type=int, default=2024)
    args = parser.parse_args()

    package_root = args.package_root.resolve()
    output_dir = args.output_dir.resolve()
    run_working_universe_build(package_root, output_dir, args.year_min, args.year_max)
    validation_summary = build_external_econ_only_audit(package_root, output_dir)
    write_run_summary(package_root, output_dir, validation_summary)
    print(json.dumps({"output_dir": str(output_dir), "validation": validation_summary}, indent=2))


if __name__ == "__main__":
    main()
