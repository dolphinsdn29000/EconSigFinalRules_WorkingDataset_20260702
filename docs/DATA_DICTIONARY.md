# Data Dictionary

This document describes the main outputs.  It is not an exhaustive column-by-
column catalog for every audit file, but it explains the fields most likely to
matter during analysis.

## Main Rule-Level File

Path:

```text
data/release_current/econ_sig_final_rules_rule_level_2000_2024.csv
```

One row is a collapsed rule group.  It is not necessarily one RIN and not
necessarily one raw Federal Register document.

Important columns:

| Column | Meaning |
|---|---|
| `rule_group_key` | Internal group id for documents treated as one rule group. |
| `presidential_year` | Presidential year convention: February 1 through January 31. |
| `representative_fr_doc_key` | Representative FR document key chosen for the rule group. |
| `representative_fr_issue_date` | Publication date of representative FR document. |
| `representative_fr_frdoc_no` | Federal Register document number. |
| `representative_fr_title` | Representative FR title/subject. |
| `representative_fr_action` | FR action text. |
| `representative_action_family` | Normalized action family used by the pipeline. |
| `representative_fr_agency_header` | FR agency header. |
| `representative_fr_cfr` | CFR metadata from local FR parsing. |
| `representative_fr_summary` | FR summary text. |
| `representative_fr_summary_abridged` | Truncated summary for easier review. |
| `econ_rin_list` | Economic-significance candidate RINs attached to the group. |
| `source_ua_any_econ_rin` | True if a local FR RIN matched a UA econ/3(f)(1) priority RIN. |
| `source_regstats_oira_linked` | True if the row was found through the external OIRA/RegStats linked source. |
| `source_systems` | Source labels that caused the row to enter the candidate universe. |
| `cfr_validation_statuses` | Whether CFR evidence came from local FR or strict external link. |
| `audited_primary` | True if final-like and locally CFR-validated. |
| `provisional_primary` | True if final-like but lacking local CFR validation. |
| `related_fr_doc_count` | Number of FR documents in the collapsed group. |
| `related_fr_doc_keys` | All related FR document keys in the group. |
| `related_fr_dates` | Publication dates for related FR documents. |
| `related_fr_titles` | Titles for related FR documents. |
| `related_fr_actions` | Action labels for related FR documents. |
| `related_source_flags` | Per-document source flags. |
| `ua_econ_priority_values` | UA econ priority labels available for group RINs. |
| `ua_rule_titles` | UA titles associated with group RINs. |
| `ua_rule_stages` | UA stages associated with group RINs. |
| `ua_final_rule_dates` | UA final-rule dates associated with group RINs. |
| `ua_nprm_dates` | UA NPRM dates associated with group RINs. |
| `ua_timetable_summary` | UA timetable text summary. |
| `oira_regstats_titles` | Titles from external OIRA/RegStats linked rows. |

## CFR-Audited Rule-Level File

Path:

```text
data/release_current/econ_sig_final_rules_rule_level_2000_2024_cfr_audited.csv
```

Same schema as the main rule-level file, but restricted to rows with
`audited_primary=True`.

This is the safest file for analysis if you want to avoid provisional rows.

## Document Candidate File

Path:

```text
data/release_current/econ_sig_final_rule_document_candidates_2000_2024.csv
```

One row is one Federal Register document candidate before rule-level grouping.

Important columns:

| Column | Meaning |
|---|---|
| `fr_doc_key` | Publication date plus FR document number. |
| `fr_issue_date` | FR publication date. |
| `fr_frdoc_no` | FR document number. |
| `fr_doc_type` | Federal Register document type. |
| `fr_subject` | Title/subject. |
| `fr_action` | Raw action label. |
| `action_family` | Normalized action family. |
| `fr_cfr` | CFR metadata. |
| `local_fr_rin_list` | RINs extracted from local FR parse. |
| `candidate_rin_list` | All candidate RINs from local and external evidence. |
| `candidate_econ_rin_list` | RINs used as economic-significance candidates. |
| `source_ua_any_econ_rin` | Candidate entered through UA econ priority. |
| `source_regstats_oira_linked` | Candidate entered through external OIRA/RegStats link. |
| `final_like_action` | Whether action family is primary final-like. |
| `primary_exclusion_reason` | Reason a nonprimary action would be excluded. |
| `audited_primary` | Final-like and local CFR-validated. |
| `provisional_primary` | Final-like but lacking local CFR validation. |
| `rule_group_key` | Group id used in rule-level collapse. |

## External Econ-Only Validation Target

Path:

```text
data/release_current/audits/external_econ_only_comparison_target_2000_2024_no_major_only.csv
```

This file is the external validation comparison target.  It includes only
external economic-significance or 3(f)(1) evidence, not major-only evidence.

Important columns:

| Column | Meaning |
|---|---|
| `oira_economically_significant` | OIRA completed-review economic-significance flag. |
| `fr_tracking_econ_significant` | RegStats/FR tracking economic-significance flag. |
| `fr_tracking_3f1_significant` | RegStats/FR tracking 3(f)(1) flag. |
| `oira_major` | OIRA major flag, retained for audit but not used alone. |
| `fr_tracking_major` | RegStats/FR tracking major flag, retained for audit but not used alone. |
| `present_in_ua_priority_construction` | Whether UA-priority-only construction found the document. |

## Missing From UA-Priority Construction

Path:

```text
data/release_current/audits/external_econ_only_missing_from_ua_priority_construction_2000_2024.csv
```

Rows in the external econ-only target that were not found by UA priority alone.

Important columns:

| Column | Meaning |
|---|---|
| `target_rins` | RINs used for comparison/audit. |
| `miss_reason` | Why the UA-priority construction did not find the row. |

Common `miss_reason` values:

```text
target_rin_in_ua_but_not_ua_econ_priority
target_rin_has_ua_econ_but_doc_not_in_ua_construction_path
target_rin_not_found_in_ua
external_econ_doc_has_no_rin_in_target_record
```

## Database Views

Folder:

```text
data/release_current/database_view/
```

These are convenience outputs for inspection.  The most useful one is:

```text
econ_sig_final_rules_database_sorted_by_action_rin_date_2000_2024.csv
```

It is the rule-level dataset sorted for manual browsing.

