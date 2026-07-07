# UA Core Rebuild

This folder starts a clean Unified Agenda core rebuild for economically
significant final-rule/final-action candidates.

Step 1 is intentionally UA-only:

- it reads `source_inputs/ua_all_flat_rin_norm.csv.gz`;
- it uses embedded `ua_timetable_json` event rows as the timetable source;
- it does not match to Federal Register documents;
- it does not group Federal Register documents by RIN;
- it does not create a final FR-document dataset.

Run from the project root:

```sh
python3 ua_core_rebuild/01_build_ua_econ_final_actions.py
python3 ua_core_rebuild/02_audit_ua_econ_final_actions.py
```

Local generated outputs are written to:

```text
generated_outputs/ua_core_rebuild_step1/
```

Commit-oriented summaries are written to:

```text
docs/UA_CORE_STEP1_BUILD_SUMMARY.md
docs/UA_CORE_STEP1_AUDIT.md
```
