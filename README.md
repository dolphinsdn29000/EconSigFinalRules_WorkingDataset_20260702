# Economically Significant Final Rules Working Dataset

Package date: 2026-07-02

This folder packages the current working dataset and the pipeline needed to
rebuild it from compact parsed inputs.

The dataset is good enough for current analysis and auditing, but it should be
described honestly as a working/candidate universe.  The main remaining issue is
not Federal Register matching.  The main issue is source classification: some
rules are economically significant according to OIRA or the final-rule text even
when the Unified Agenda priority field says only `Other Significant`.

## Folder Layout

```text
EconSigFinalRules_WorkingDataset_20260702/
  README.md
  requirements.txt
  source_inputs/
    Compact parsed FR/UA/OIRA/RegStats inputs needed to rebuild the dataset.
  pipeline/
    run_econ_sig_final_rule_pipeline.py
    build_union_universe_original_snapshot.py
  data/release_current/
    The current generated dataset and audit outputs copied from the working run.
  generated_outputs/
    Rebuild outputs written here when the runner is executed.
  docs/
    Human-readable methods, validation notes, and data dictionary.
```

## Quick Rebuild

From this folder:

```bash
python3 pipeline/run_econ_sig_final_rule_pipeline.py
```

Default output:

```text
generated_outputs/rebuilt_from_packaged_inputs/econ_sig_final_rule_universe_v2/
```

The runner does two things:

1. Rebuilds the current working universe from packaged inputs.
2. Rebuilds the external econ-only validation audit, explicitly excluding
   major-only rules from the comparison target.

## Main Current Data Files

Current release files are in:

```text
data/release_current/
```

Most useful files:

```text
econ_sig_final_rules_rule_level_2000_2024.csv
econ_sig_final_rules_rule_level_2000_2024_cfr_audited.csv
econ_sig_final_rule_document_candidates_2000_2024.csv
audits/external_econ_only_comparison_target_2000_2024_no_major_only.csv
audits/external_econ_only_missing_from_ua_priority_construction_2000_2024.csv
database_view/econ_sig_final_rules_database_sorted_by_action_rin_date_2000_2024.csv
```

## Current Counts

Current release, rule level:

```text
Rule rows: 1,574
CFR-audited rule rows: 1,572
FR document candidates: 1,751
Unique RINs across rule rows: 1,601
Rows with multiple RINs: 95
Rows with blank econ_rin_list: 4
```

Current release source mix:

```text
UA econ priority + external source: 1,024
UA econ priority only: 430
External source only: 120
```

External econ-only validation target:

```text
External econ-only target docs: 1,157
Found by UA-priority construction: 1,039
Missing from UA-priority construction: 118
Major-only records included in comparison: 0
```

## Important Interpretation

The current release intentionally preserves enough evidence to audit the data.
It should not be summarized as "the final truth" without describing the evidence
hierarchy.

The defensible statement is:

> This package contains a working universe of economically significant final-rule
> candidates linked to Federal Register and Unified Agenda data, with external
> OIRA/RegStats evidence retained for validation and conflict auditing.

The most important caution:

> `major` alone is not used as the target category.  The target is economically
> significant or Section 3(f)(1), not all major rules.

See `docs/METHODS_AND_DECISIONS.md` for the reasoning.

