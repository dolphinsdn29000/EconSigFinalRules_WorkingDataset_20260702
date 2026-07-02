# Data Manifest

Project root:

```text
/Volumes/OWC Envoy Pro FX/EconSigFinalRules_WorkingDataset_20260702
```

This repository is intended for code, configuration, and documentation sync
through GitHub. Large, raw, generated, or sensitive data remain local in the
project folder above and are excluded from git by `.gitignore`.

## Local Data Folders

### `source_inputs/`

Compact parsed input files used by the local rebuild pipeline. This folder
contains parsed Federal Register, Unified Agenda, and OIRA/RegStats linkage
tables. These are data inputs and should remain local unless explicitly approved.

Observed examples:

```text
fr_final_rules_rawparsed.csv.gz
fr_final_rules_rin_exploded.csv.gz
ua_all_flat_rin_norm.csv.gz
econ_sig_final_rules_STRICT_FR_RULE_2000_forward_linked_full.csv
econ_significant_rules_by_presidential_year.csv
```

### `data/release_current/`

Current generated working dataset release and inspection/audit outputs. This
folder contains rule-level CSVs, document-candidate CSVs, audit CSVs, database
views, profiles, and charts. It is generated/release data and should remain
local.

### `generated_outputs/`

Rebuild outputs produced by `pipeline/run_econ_sig_final_rule_pipeline.py`.
These files are reproducible from local `source_inputs/` and should remain out
of git.

## Code/Documentation Intended For Git

Safe files for GitHub code visibility include:

```text
README.md
DATA_MANIFEST.md
AGENTS.md
requirements.txt
docs/*.md
pipeline/*.py
.gitignore
```

## Policy

Do not stage or upload raw data, generated datasets, model files, archives,
PDFs, credentials, or large binary files. If a future workflow requires sharing
data, create a separate explicit data-transfer plan rather than using this code
repository.

