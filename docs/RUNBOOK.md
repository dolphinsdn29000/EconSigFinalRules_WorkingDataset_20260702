# Runbook

## Rebuild Command

From the package root:

```bash
python3 pipeline/run_econ_sig_final_rule_pipeline.py
```

Default output:

```text
generated_outputs/rebuilt_from_packaged_inputs/econ_sig_final_rule_universe_v2/
```

## Verified Rebuild

The packaged runner was executed on 2026-07-02.  The rebuilt substantive CSVs
matched the copied current release byte-for-byte for:

```text
econ_sig_final_rule_document_candidates_2000_2024.csv
econ_sig_final_rules_rule_level_2000_2024.csv
econ_sig_final_rules_rule_level_2000_2024_cfr_audited.csv
econ_sig_final_rules_multi_document_groups_audit.csv
econ_sig_final_rule_provisional_or_uncfr_validated_docs_audit.csv
excluded_out_of_scope_presidential_years_audit.csv
econ_sig_final_rule_counts_vs_regstats.csv
audits/external_econ_only_comparison_target_2000_2024_no_major_only.csv
audits/external_econ_only_missing_from_ua_priority_construction_2000_2024.csv
audits/external_major_only_excluded_from_comparison_2000_2024.csv
```

The rebuilt headline counts were:

```text
Document candidates: 1,751
CFR-audited document candidates: 1,749
Rule groups: 1,574
CFR-audited rule groups: 1,572
Multi-document rule groups: 92
External econ-only target docs: 1,157
Missing from UA-priority construction: 118
Major-only records included in econ-only target: 0
```

## Which File To Use

For most analysis:

```text
data/release_current/econ_sig_final_rules_rule_level_2000_2024_cfr_audited.csv
```

For manual inspection:

```text
data/release_current/database_view/econ_sig_final_rules_database_sorted_by_action_rin_date_2000_2024.csv
```

For understanding source disagreements:

```text
data/release_current/audits/external_econ_only_missing_from_ua_priority_construction_2000_2024.csv
```

For reproducibility:

```text
source_inputs/
pipeline/run_econ_sig_final_rule_pipeline.py
pipeline/build_union_universe_original_snapshot.py
```

## File Manifest

The package root contains:

```text
PACKAGE_FILE_MANIFEST.tsv
```

It lists SHA-256 checksums for packaged files.

