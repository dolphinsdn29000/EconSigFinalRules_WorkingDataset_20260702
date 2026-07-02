# Project Instructions For Codex / ChatGPT

Project root:

```text
/Volumes/OWC Envoy Pro FX/EconSigFinalRules_WorkingDataset_20260702
```

## Core Rules

- Preserve the exact project path above.
- Treat this as a code-sync project, not a data-upload project.
- Do not move, delete, rename, or reformat original data files.
- Do not modify raw/input/generated data unless the user explicitly asks.
- Do not upload data to GitHub.
- Do not stage raw data, generated datasets, model files, archives, PDFs, or
  private credentials.
- Summarize intended changes before commits.
- Show `git status --short` and `git diff --cached --stat` before commits.
- Ask the user for confirmation before committing or pushing.
- Use GitHub for code visibility.
- Use Dropbox Backup only for disaster recovery, not active collaboration.

## Safe Git Scope

Safe code/config/docs files include:

```text
.py
.R
.r
.Rmd
.rmd
.qmd
.do
.sh
.sql
.md
.txt
.yaml
.yml
.json
.toml
.ini
requirements.txt
pyproject.toml
renv.lock
DESCRIPTION
AGENTS.md
```

Even if a file has a safe extension, do not stage it if it lives inside a local
data/output directory such as `data/`, `source_inputs/`, or
`generated_outputs/`.

## Current Dataset Status

The project packages a working/candidate universe of economically significant
final-rule records. The current pipeline is reproducible from local packaged
inputs, but the generated data remain local-only. The key methodological caveat
is that Unified Agenda priority alone misses some rules that OIRA or final-rule
text classify as economically significant.

