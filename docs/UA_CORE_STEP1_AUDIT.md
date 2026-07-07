# UA Core Step 1 Audit

This audit treats old document-level and rule-level files as comparison baselines, not truth sources.

## Summary Counts

- Strict UA-core base rows: 3,614
- Distinct RINs in base: 1,603
- Rows with explicit FR citations: 1,382
- Uncertain/excluded event rows: 36,160
- Possible missing/suspicious rows written: 12,858
- Section 3(f)(1) base rows: 376

## Section 3(f)(1) Years

Section 3(f)(1) rows are included for review because 2023-2024 may use that label for the economic prong. Pre-2023 final-action years can appear when a 2023-2024 UA vintage carries older timetable history.

| final_action_year | section_3f1_row_count |
| --- | --- |
| 2017 | 1 |
| 2018 | 1 |
| 2019 | 1 |
| 2020 | 1 |
| 2021 | 3 |
| 2022 | 1 |
| 2023 | 81 |
| 2024 | 287 |

## Counts Table Preview

| comparison | year_type | year | count | notes |
| --- | --- | --- | --- | --- |
| new_ua_core_base | calendar_year | ALL | 3614 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2000 | 105 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2001 | 85 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2002 | 89 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2003 | 90 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2004 | 92 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2005 | 90 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2006 | 84 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2007 | 119 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2008 | 161 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2009 | 135 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2010 | 151 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2011 | 159 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2012 | 108 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2013 | 153 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2014 | 142 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2015 | 171 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2016 | 227 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2017 | 79 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2018 | 93 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2019 | 122 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2020 | 189 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2021 | 202 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2022 | 194 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2023 | 259 | Strict UA-core final-action candidates; not FR documents. |
| new_ua_core_base | calendar_year | 2024 | 315 | Strict UA-core final-action candidates; not FR documents. |
| data/release_current/econ_sig_final_rule_document_candidates_2000_2024.csv | all_rows_or_records | ALL | 1751 | Baseline only; distinct extracted RINs=1692, overlap with new base=1277. |
| data/release_current/econ_sig_final_rule_document_candidates_2000_2024.csv | calendar_year | 2000 | 56 | Baseline count; not authoritative for UA-core. |
| data/release_current/econ_sig_final_rule_document_candidates_2000_2024.csv | calendar_year | 2001 | 63 | Baseline count; not authoritative for UA-core. |
| data/release_current/econ_sig_final_rule_document_candidates_2000_2024.csv | calendar_year | 2002 | 43 | Baseline count; not authoritative for UA-core. |

## Internal Issue Counts

| issue_type | count |
| --- | --- |
| baseline_rin_absent_from_new_ua_core_base | 2443 |
| final_action_date_outside_2000_2024 | 2415 |
| missing_fr_citation_in_strict_base | 2232 |
| partial_or_non_exact_final_action_date | 2226 |
| same_rin_legacy_econ_and_non_econ_priority_across_vintages | 1199 |
| econ_prong_rin_has_no_strict_base_final_action | 934 |
| same_rin_multiple_final_action_dates | 932 |
| same_rin_legacy_econ_and_section_3f1_priority_across_vintages | 241 |
| oira_or_regstats_econ_final_rin_absent_from_new_ua_core_base | 199 |
| unparseable_timetable_or_date | 25 |
| section_3f1_priority_on_pre_2023_final_action_year | 8 |
| included_label_has_excluded_term | 4 |

## 20 Clean Included Records

| ua_base_id | rin_norm | final_action_year | ua_priority_category | ua_rule_title | final_action_label | final_action_fr_citation_raw |
| --- | --- | --- | --- | --- | --- | --- |
| UA-ECON-FINAL-000011 | 0560-AG13 | 2000 | Economically Significant | 1999 Crop and Market Loss Assistance | Final Action | 65 FR 7942 |
| UA-ECON-FINAL-000079 | 0560-AG16 | 2000 | Economically Significant | Bioenergy Program | Final Rule | 65 FR 67608 |
| UA-ECON-FINAL-000076 | 0560-AG18 | 2000 | Economically Significant | 2000-Crop Agricultural Disaster and Market Assistance | Final Rule | 65 FR 65709 |
| UA-ECON-FINAL-000077 | 0560-AG19 | 2000 | Economically Significant | Market Assistance for Tobacco, Wool and Mohair, and Cottonseed | Final Rule | 65 FR 64718 |
| UA-ECON-FINAL-000069 | 0563-AB81 | 2000 | Economically Significant | Catastrophic Risk Protection Endorsement; Group Risk Plan of Insurance Regulations; Basic Provisions | Final Rule |  |
| UA-ECON-FINAL-000084 | 0581-AA40 | 2000 | Economically Significant | National Organic Program | Final Action |  |
| UA-ECON-FINAL-000102 | 0581-AA40 | 2000 | Economically Significant | National Organic Program | Final Action | 65 FR 80548 |
| UA-ECON-FINAL-000055 | 0581-AB64 | 2000 | Economically Significant | Livestock Mandatory Reporting Act of 1999 | Final Action |  |
| UA-ECON-FINAL-000101 | 0581-AB64 | 2000 | Economically Significant | Livestock Mandatory Reporting Act of 1999 | Final Action | 65 FR 75463 |
| UA-ECON-FINAL-000005 | 0583-AC26 | 2000 | Economically Significant | Retained Water in Raw Meat and Poultry Products; Poultry-Chilling Performance Standards | Final Action |  |
| UA-ECON-FINAL-000085 | 0583-AC26 | 2000 | Economically Significant | Retained Water in Raw Meat and Poultry Products; Poultry-Chilling Performance Standards | Final Action |  |
| UA-ECON-FINAL-000035 | 0584-AB52 | 2000 | Economically Significant | WIC: Requirements for and Evaluation of WIC Program Requests for Bids for Infant Formula Rebate Contracts | Final Action |  |
| UA-ECON-FINAL-000001 | 0584-AB88 | 2000 | Economically Significant | Food Stamp Program: Food Stamp Recipient Claim Establishment and Collection Standards | Final Action |  |
| UA-ECON-FINAL-000015 | 0584-AB88 | 2000 | Economically Significant | Food Stamp Program: Food Stamp Recipient Claim Establishment and Collection Standards | Final Action |  |
| UA-ECON-FINAL-000056 | 0584-AC39 | 2000 | Economically Significant | FSP: Personal Responsibility Provisions of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 | Final Action |  |
| UA-ECON-FINAL-000057 | 0584-AC40 | 2000 | Economically Significant | FSP: Noncitizen Eligibility and Certification Provisions of Public Law 104-193 (Previously Entitled State Flexibility and Certification Provisions) | Final Action |  |
| UA-ECON-FINAL-000082 | 0584-AC40 | 2000 | Economically Significant | FSP: Noncitizen Eligibility and Certification Provisions of Public Law 104-193 (Previously Entitled State Flexibility and Certification Provisions) | Final Action | 65 FR 70134 |
| UA-ECON-FINAL-000040 | 0584-AC41 | 2000 | Economically Significant | FSP: Nondiscretionary Provisions of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 | Final Action |  |
| UA-ECON-FINAL-000058 | 0584-AC41 | 2000 | Economically Significant | FSP: Nondiscretionary Provisions of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 | Final Action |  |
| UA-ECON-FINAL-000067 | 0584-AC41 | 2000 | Economically Significant | FSP: Nondiscretionary Provisions of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 | Final Action | 65 FR 64581 |

## 20 Excluded Records With Reasons

| rin_norm | ua_priority_category | ua_rule_stage | final_action_label | final_action_date_raw | exclusion_reason |
| --- | --- | --- | --- | --- | --- |
| 0551-AA27 | Economically Significant | Final Rule Stage | Interim Final Rule | 05/02/1995 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Final Rule Stage | ANPRM | 06/02/1994 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Final Rule Stage | ANPRM Comment Period End | 08/01/1994 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Final Rule Stage | Interim Final Rule | 09/13/1995 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Final Rule Stage | Interim Final Rule | 10/00/1995 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Final Rule Stage | NPRM | 01/18/1996 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Final Rule Stage | NPRM Comment Period End | 03/18/1996 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Final Rule Stage | Interim Final Rule | 05/02/1995 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Final Rule Stage | ANPRM | 06/02/1994 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Final Rule Stage | Final Action | 07/00/1996 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Final Rule Stage | ANPRM Comment Period End | 08/01/1994 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Final Rule Stage | Interim Final Rule | 09/13/1995 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Completed Actions | NPRM | 01/18/1996 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Completed Actions | NPRM Comment Period End | 03/18/1996 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Completed Actions | Interim Final Rule | 05/02/1995 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Completed Actions | ANPRM | 06/02/1994 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Completed Actions | ANPRM Comment Period End | 08/01/1994 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Completed Actions | Interim Final Rule | 09/13/1995 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Completed Actions | Final Action | 10/09/1996 | final_action_year_outside_2000_2024 |
| 0551-AA27 | Economically Significant | Completed Actions | Final Action Effective | 10/09/1996 | final_action_year_outside_2000_2024 |

## 20 Uncertain/Ambiguous Records

| issue_type | rin_norm | final_action_year | final_action_date_raw | final_action_label | details |
| --- | --- | --- | --- | --- | --- |
| uncertain_excluded_event | 0551-AA27 | 1995 | 05/02/1995 | Interim Final Rule | final_action_year_outside_2000_2024: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 09/13/1995 | Interim Final Rule | final_action_year_outside_2000_2024: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 10/00/1995 | Interim Final Rule | final_action_year_outside_2000_2024: Interim final rule kept outside strict base. / month_year_only_zero_day |
| uncertain_excluded_event | 0551-AA27 | 1995 | 05/02/1995 | Interim Final Rule | final_action_year_outside_2000_2024: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 09/13/1995 | Interim Final Rule | final_action_year_outside_2000_2024: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 05/02/1995 | Interim Final Rule | stage_not_final_or_completed: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 09/13/1995 | Interim Final Rule | stage_not_final_or_completed: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 05/02/1995 | Interim Final Rule | stage_not_final_or_completed: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 09/13/1995 | Interim Final Rule | stage_not_final_or_completed: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 05/02/1995 | Interim Final Rule | stage_not_final_or_completed: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 09/13/1995 | Interim Final Rule | stage_not_final_or_completed: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 05/02/1995 | Interim Final Rule | stage_not_final_or_completed: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 09/13/1995 | Interim Final Rule | stage_not_final_or_completed: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 05/02/1995 | Interim Final Rule | stage_not_final_or_completed: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 09/13/1995 | Interim Final Rule | stage_not_final_or_completed: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 05/02/1995 | Interim Final Rule | final_action_year_outside_2000_2024: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA27 | 1995 | 09/13/1995 | Interim Final Rule | final_action_year_outside_2000_2024: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA30 | 1991 | 06/06/1991 | Interim Final Rule | final_action_year_outside_2000_2024: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA30 | 1991 | 06/06/1991 | Interim Final Rule | final_action_year_outside_2000_2024: Interim final rule kept outside strict base. |
| uncertain_excluded_event | 0551-AA30 | 1996 | 07/01/1996 | Interim Final Rule | final_action_year_outside_2000_2024: Interim final rule kept outside strict base. |

## 20 Possible Missing Records

| issue_type | rin_norm | ua_priority_category | ua_rule_title | details | source_file | comparison_value |
| --- | --- | --- | --- | --- | --- | --- |
| baseline_rin_absent_from_new_ua_core_base | 0412-AB10 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | data/release_current/econ_sig_final_rule_document_candidates_2000_2024.csv | baseline_rins=1692; overlap=1277 |
| baseline_rin_absent_from_new_ua_core_base | 0412-AB10 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | generated_outputs/rebuilt_from_packaged_inputs/econ_sig_final_rule_universe_v2/econ_sig_final_rule_document_candidates_2000_2024.csv | baseline_rins=1692; overlap=1277 |
| baseline_rin_absent_from_new_ua_core_base | 0551-AA63 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | data/release_current/econ_sig_final_rule_document_candidates_2000_2024.csv | baseline_rins=1692; overlap=1277 |
| baseline_rin_absent_from_new_ua_core_base | 0551-AA63 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | data/release_current/econ_sig_final_rules_rule_level_2000_2024.csv | baseline_rins=1601; overlap=1277 |
| baseline_rin_absent_from_new_ua_core_base | 0551-AA63 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | data/release_current/econ_sig_final_rules_rule_level_2000_2024_cfr_audited.csv | baseline_rins=1599; overlap=1276 |
| baseline_rin_absent_from_new_ua_core_base | 0551-AA63 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | generated_outputs/rebuilt_from_packaged_inputs/econ_sig_final_rule_universe_v2/econ_sig_final_rule_document_candidates_2000_2024.csv | baseline_rins=1692; overlap=1277 |
| baseline_rin_absent_from_new_ua_core_base | 0551-AA63 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | generated_outputs/rebuilt_from_packaged_inputs/econ_sig_final_rule_universe_v2/econ_sig_final_rules_rule_level_2000_2024.csv | baseline_rins=1601; overlap=1277 |
| baseline_rin_absent_from_new_ua_core_base | 0551-AA63 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | generated_outputs/rebuilt_from_packaged_inputs/econ_sig_final_rule_universe_v2/econ_sig_final_rules_rule_level_2000_2024_cfr_audited.csv | baseline_rins=1599; overlap=1276 |
| baseline_rin_absent_from_new_ua_core_base | 0551-AA63 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | source_inputs/econ_sig_final_rules_STRICT_FR_RULE_2000_forward_linked_full.csv | baseline_rins=1506; overlap=1187 |
| baseline_rin_absent_from_new_ua_core_base | 0560-AF48 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | data/release_current/econ_sig_final_rule_document_candidates_2000_2024.csv | baseline_rins=1692; overlap=1277 |
| baseline_rin_absent_from_new_ua_core_base | 0560-AF48 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | data/release_current/econ_sig_final_rules_rule_level_2000_2024.csv | baseline_rins=1601; overlap=1277 |
| baseline_rin_absent_from_new_ua_core_base | 0560-AF48 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | data/release_current/econ_sig_final_rules_rule_level_2000_2024_cfr_audited.csv | baseline_rins=1599; overlap=1276 |
| baseline_rin_absent_from_new_ua_core_base | 0560-AF48 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | generated_outputs/rebuilt_from_packaged_inputs/econ_sig_final_rule_universe_v2/econ_sig_final_rule_document_candidates_2000_2024.csv | baseline_rins=1692; overlap=1277 |
| baseline_rin_absent_from_new_ua_core_base | 0560-AF48 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | generated_outputs/rebuilt_from_packaged_inputs/econ_sig_final_rule_universe_v2/econ_sig_final_rules_rule_level_2000_2024.csv | baseline_rins=1601; overlap=1277 |
| baseline_rin_absent_from_new_ua_core_base | 0560-AF48 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | generated_outputs/rebuilt_from_packaged_inputs/econ_sig_final_rule_universe_v2/econ_sig_final_rules_rule_level_2000_2024_cfr_audited.csv | baseline_rins=1599; overlap=1276 |
| baseline_rin_absent_from_new_ua_core_base | 0560-AF48 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | source_inputs/econ_sig_final_rules_STRICT_FR_RULE_2000_forward_linked_full.csv | baseline_rins=1506; overlap=1187 |
| baseline_rin_absent_from_new_ua_core_base | 0560-AG14 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | source_inputs/econ_sig_final_rules_STRICT_FR_RULE_2000_forward_linked_full.csv | baseline_rins=1506; overlap=1187 |
| baseline_rin_absent_from_new_ua_core_base | 0560-AH45 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | data/release_current/econ_sig_final_rule_document_candidates_2000_2024.csv | baseline_rins=1692; overlap=1277 |
| baseline_rin_absent_from_new_ua_core_base | 0560-AH45 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | data/release_current/econ_sig_final_rules_rule_level_2000_2024.csv | baseline_rins=1601; overlap=1277 |
| baseline_rin_absent_from_new_ua_core_base | 0560-AH45 |  |  | RIN appears in local comparison baseline but not strict UA-core base. | data/release_current/econ_sig_final_rules_rule_level_2000_2024_cfr_audited.csv | baseline_rins=1599; overlap=1276 |

## Section 3(f)(1) Examples

| ua_base_id | rin_norm | final_action_year | ua_rule_title | final_action_label | final_action_date_raw |
| --- | --- | --- | --- | --- | --- |
| UA-ECON-FINAL-002197 | 3084-AB46 | 2017 | Premerger Notification Rules and Report Form | Final Rule (HSR Form Update) | 07/12/2017 |
| UA-ECON-FINAL-002272 | 3084-AB46 | 2018 | Premerger Notification Rules and Report Form | Final Rule (HSR Form Instructions Update) | 07/16/2018 |
| UA-ECON-FINAL-002382 | 3084-AB46 | 2019 | Premerger Notification Rules and Report Form | Final Rule (HSR Form Instructions Update) | 06/27/2019 |
| UA-ECON-FINAL-002641 | 0790-AK85 | 2020 | National Industrial Security Program Operating Manual (NISPOM) | Final Action | 12/21/2020 |
| UA-ECON-FINAL-002663 | 1205-AC00 | 2021 | Strengthening Wage Protections for the Temporary and Permanent Employment of Certain Aliens in the United States | Final Rule | 01/14/2021 |
| UA-ECON-FINAL-002739 | 0790-AK85 | 2021 | National Industrial Security Program Operating Manual (NISPOM) | Final Rule Amendment | 08/19/2021 |
| UA-ECON-FINAL-002839 | 1205-AC00 | 2021 | Strengthening Wage Protections for the Temporary and Permanent Employment of Certain Aliens in the United States | Final Rule (Implementation of Court's Vacatur of Final Rule) | 12/13/2021 |
| UA-ECON-FINAL-002988 | 0625-AB21 | 2022 | Procedures Covering Suspension of Liquidation, Duties and Estimated Duties in Accord with Presidential Proclamation 10414 / Procedures Covering Suspension of Liquidation, Duties an | Final Action | 09/16/2022 |
| UA-ECON-FINAL-003056 | 2900-AQ08 | 2023 | Reimbursement for Emergency Treatment | Final Action | 02/22/2023 |
| UA-ECON-FINAL-003078 | 1904-AF46 | 2023 | Energy Conservation Standards for Air Cleaners | Direct Final Rule | 04/11/2023 |
| UA-ECON-FINAL-003080 | 0938-AU97 | 2023 | HHS Notice of Benefit and Payment Parameters for 2024 (CMS-9899) | Final Action | 04/27/2023 |
| UA-ECON-FINAL-003141 | 1904-AE63 | 2023 | Energy Conservation Standards for Electric Motors | Direct Final Rule | 06/01/2023 |
| UA-ECON-FINAL-003142 | 0938-AU75 | 2023 | Omnibus COVID-19 Health Care Staff Vaccination (CMS-3415) | Final Action | 06/05/2023 |
| UA-ECON-FINAL-003143 | 2060-AV51 | 2023 | Federal “Good Neighbor Plan” for the 2015 Ozone National Ambient Air Quality Standards | Final Rule | 06/05/2023 |
| UA-ECON-FINAL-003144 | 0938-AU24 | 2023 | Treatment of Medicare Part C Days in the Calculation of a Hospital's Medicare Disproportionate Patient Percentage (CMS-1739) | Final Action | 06/09/2023 |
| UA-ECON-FINAL-003145 | 3150-AK58 | 2023 | Revision of Fee Schedules: Fee Recovery for FY 2023 [NRC-2021-0024] | Final Rule | 06/15/2023 |
| UA-ECON-FINAL-003156 | 1840-AD81 | 2023 | Improving Income Driven Repayment | Final Action | 07/10/2023 |
| UA-ECON-FINAL-003157 | 2060-AV14 | 2023 | Renewable Fuel Standard (RFS) Program: Standards for 2023–2025 and Other Changes | Final Rule | 07/12/2023 |
| UA-ECON-FINAL-003158 | 2060-AV45 | 2023 | Phasedown of Hydrofluorocarbons: Allowance Allocation Methodology for 2024 and Later Years | Final Rule | 07/20/2023 |
| UA-ECON-FINAL-003159 | 1117-AB45 | 2023 | Partial Filling of Prescriptions for Schedule II Controlled Substances | Final Action | 07/21/2023 |

## RINs With Multiple Final-Action Dates

| issue_type | rin_norm | details | comparison_value |
| --- | --- | --- | --- |
| same_rin_multiple_final_action_dates | 0331-AA07 | 04/00/2024 / 05/01/2024 | 2 |
| same_rin_multiple_final_action_dates | 0503-AA65 | 05/21/2020 / 09/22/2020 | 2 |
| same_rin_multiple_final_action_dates | 0503-AA71 | 05/00/2021 / 08/27/2021 | 2 |
| same_rin_multiple_final_action_dates | 0503-AA73 | 01/00/2024 / 03/04/2024 | 2 |
| same_rin_multiple_final_action_dates | 0503-AA75 | 11/00/2021 / 09/00/2022 / 12/00/2022 / 01/11/2023 | 4 |
| same_rin_multiple_final_action_dates | 0560-AG20 | 03/19/2002 / 08/00/2002 | 2 |
| same_rin_multiple_final_action_dates | 0560-AG71 | 10/01/2002 / 10/21/2002 / 02/03/2003 | 3 |
| same_rin_multiple_final_action_dates | 0560-AG72 | 10/11/2002 / 10/18/2002 | 2 |
| same_rin_multiple_final_action_dates | 0560-AG74 | 12/00/2002 / 05/14/2004 | 2 |
| same_rin_multiple_final_action_dates | 0560-AG95 | 06/00/2003 / 06/26/2003 | 2 |
| same_rin_multiple_final_action_dates | 0560-AH43 | 12/00/2007 / 06/00/2008 / 02/00/2009 / 09/00/2009 / 01/00/2010 / 12/00/2010 / 05/00/2011 | 7 |
| same_rin_multiple_final_action_dates | 0560-AH60 | 11/00/2008 / 07/00/2009 | 2 |
| same_rin_multiple_final_action_dates | 0560-AH84 | 11/00/2008 / 12/29/2008 | 2 |
| same_rin_multiple_final_action_dates | 0560-AH86 | 04/06/2009 / 06/27/2013 | 2 |
| same_rin_multiple_final_action_dates | 0560-AH87 | 11/00/2008 / 04/01/2009 | 2 |
| same_rin_multiple_final_action_dates | 0560-AH90 | 10/00/2009 / 12/00/2009 / 12/28/2009 | 3 |
| same_rin_multiple_final_action_dates | 0560-AI37 | 06/00/2019 / 06/18/2019 | 2 |
| same_rin_multiple_final_action_dates | 0560-AI39 | 07/00/2018 / 07/18/2018 | 2 |
| same_rin_multiple_final_action_dates | 0560-AI40 | 05/00/2018 / 08/16/2018 | 2 |
| same_rin_multiple_final_action_dates | 0560-AI55 | 10/00/2020 / 12/00/2020 / 01/06/2021 | 3 |

## Examples With Explicit FR Citations

| ua_base_id | rin_norm | final_action_year | final_action_label | final_action_fr_citation_raw | ua_rule_title |
| --- | --- | --- | --- | --- | --- |
| UA-ECON-FINAL-000003 | 2060-AH88 | 2000 | Final Rule | 65 FR 2674 | Findings of Significant Contribution and Rulemaking on Section 126 Petitions for Purposes of Reducing Interstate Ozone Transport |
| UA-ECON-FINAL-000004 | 2060-AJ20 | 2000 | Final Action Section 126 Approvals and Remedy | 65 FR 2674 | Rulemakings for the Purpose of Reducing Interstate Ozone Transport / Overview of Rulemakings for the Purpose of Reducing Interstate Ozone Transport |
| UA-ECON-FINAL-000009 | 1210-AA52 | 2000 | Final Action Forms | 65 FR 5026 | Revision of the Form 5500 Series and Implementing and Related Regulations Under the Employee Retirement Income Security Act of 1974 (ERISA) |
| UA-ECON-FINAL-000010 | 2060-AI23 | 2000 | Final Action | 65 FR 6698 | Tier II Light-Duty Vehicle and Light-Duty Truck Emission Standards and Gasoline Sulfur Standards |
| UA-ECON-FINAL-000011 | 0560-AG13 | 2000 | Final Action | 65 FR 7942 | 1999 Crop and Market Loss Assistance |
| UA-ECON-FINAL-000024 | 2127-AH95 | 2000 | Final Action | 65 FR 17776 | Light Truck Fuel Economy Standards for Model Year 2002 |
| UA-ECON-FINAL-000025 | 0938-AI56 | 2000 | Final Action | 65 FR 18434 | Prospective Payment System for Hospital Outpatient Services (HCFA-1005-F) |
| UA-ECON-FINAL-000026 | 2060-AE29 | 2000 | Final Action Hand-held engines | 65 FR 24267 | Nonroad Spark-Ignition Engines At or Below 19 Kilowatts (25 Horsepower) (Phase 2) |
| UA-ECON-FINAL-000028 | 2127-AG70 | 2000 | Final Action | 65 FR 30679 | Advanced Air Bags |
| UA-ECON-FINAL-000033 | 3150-AG26 | 2000 | Final Action | 65 FR 34913 | ECCS Evaluations Models |
| UA-ECON-FINAL-000034 | 3150-AG50 | 2000 | Final Action | 65 FR 36945 | Revision of Fee Schedules; 100 Percent Fee Recovery, FY 2000 |
| UA-ECON-FINAL-000038 | 1902-AB98 | 2000 | Final Rule | 65 FR 45859 | Well Category Determinations |
| UA-ECON-FINAL-000039 | 0938-AJ93 | 2000 | Final Action | 65 FR 46770 | Prospective Payment System and Consolidated Billing for Skilled Nursing Facilities-Update (HCFA-1112-F) |
| UA-ECON-FINAL-000045 | 0938-AK09 | 2000 | Final Rule | 65 FR 47054 | Changes to the Hospital Inpatient Perspective Payment Systems and Fiscal Year 2001 Rates (HCFA-1118-F) |
| UA-ECON-FINAL-000046 | 1018-AG08 | 2000 | Final Rule | 65 FR 51495 | Migratory Bird Hunting; Proposed 2000-01 Migratory Game Bird Hunting Regulations (Preliminary) With Requests for Indian Tribal Proposals |
| UA-ECON-FINAL-000047 | 0970-AB66 | 2000 | Final Action | 65 FR 52814 | Bonus To Reward High Performance States Under the Temporary Assistance for Needy Families Block Grant |
| UA-ECON-FINAL-000051 | 1018-AG08 | 2000 | Final Rule | 65 FR 53190 / 65 FR 53491 | Migratory Bird Hunting; Proposed 2000-01 Migratory Game Bird Hunting Regulations (Preliminary) With Requests for Indian Tribal Proposals |
| UA-ECON-FINAL-000052 | 1904-AA75 | 2000 | Final Action | 65 FR 56740 | Energy Efficiency Standards for Lamp Ballasts |
| UA-ECON-FINAL-000053 | 1018-AG08 | 2000 | Final Rule | 65 FR 58151 | Migratory Bird Hunting; Proposed 2000-01 Migratory Game Bird Hunting Regulations (Preliminary) With Requests for Indian Tribal Proposals |
| UA-ECON-FINAL-000054 | 1018-AG08 | 2000 | Final Rule | 65 FR 58313 | Migratory Bird Hunting; Proposed 2000-01 Migratory Game Bird Hunting Regulations (Preliminary) With Requests for Indian Tribal Proposals |

## Examples Without FR Citations

| ua_base_id | rin_norm | final_action_year | final_action_label | final_action_date_raw | ua_rule_title |
| --- | --- | --- | --- | --- | --- |
| UA-ECON-FINAL-000001 | 0584-AB88 | 2000 | Final Action | 01/00/2000 | Food Stamp Program: Food Stamp Recipient Claim Establishment and Collection Standards |
| UA-ECON-FINAL-000002 | 0910-AE35 | 2000 | Final Action | 01/00/2000 | HACCP for Juice |
| UA-ECON-FINAL-000005 | 0583-AC26 | 2000 | Final Action | 02/00/2000 | Retained Water in Raw Meat and Poultry Products; Poultry-Chilling Performance Standards |
| UA-ECON-FINAL-000006 | 0938-AI56 | 2000 | Final Action | 02/00/2000 | Medicare Program; Prospective Payment System for Hospital Outpatient Services (HCFA-1005-F) |
| UA-ECON-FINAL-000007 | 0991-AB08 | 2000 | Final Action | 02/00/2000 | Standards for Privacy of Individually Indentifiable Health Information |
| UA-ECON-FINAL-000008 | 2070-AC46 | 2000 | Final Action | 02/00/2000 | Ground Water and Pesticide Management Plan |
| UA-ECON-FINAL-000012 | 0938-AI59 | 2000 | Final Action | 03/00/2000 | National Standard Employer Identifier (HCFA-0047-F) |
| UA-ECON-FINAL-000013 | 2060-AE29 | 2000 | Final Action Hand-held engines | 03/00/2000 | Nonroad Spark-Ignition Engines At or Below 19 Kilowatts (25 Horsepower) (Phase 2) |
| UA-ECON-FINAL-000014 | 2127-AG70 | 2000 | Final Action | 03/00/2000 | Advanced Air Bags |
| UA-ECON-FINAL-000015 | 0584-AB88 | 2000 | Final Action | 04/00/2000 | Food Stamp Program: Food Stamp Recipient Claim Establishment and Collection Standards |
| UA-ECON-FINAL-000016 | 0648-AM59 | 2000 | Final Action | 04/00/2000 | Rule Governing the Take of Seven Threatened Evolutionarily Significant Units (ESUs) of West Coast Salmonids |
| UA-ECON-FINAL-000017 | 0910-AE35 | 2000 | Final Action | 04/00/2000 | HACCP for Juice |
| UA-ECON-FINAL-000018 | 1210-AA52 | 2000 | Final Action Implementing Related Regulations | 04/00/2000 | Revision of the Form 5500 Series and Implementing and Related Regulations Under the Employee Retirement Income Security Act of 1974 (ERISA) |
| UA-ECON-FINAL-000019 | 2060-AE29 | 2000 | Final Action Hand-held engines | 04/00/2000 | Nonroad Spark-Ignition Engines At or Below 19 Kilowatts (25 Horsepower) (Phase 2) |
| UA-ECON-FINAL-000020 | 2070-AD38 | 2000 | Final Action | 04/00/2000 | TRI; Lowering of EPCRA Section 313 Reporting Thresholds for Lead and Lead Compounds |
| UA-ECON-FINAL-000021 | 2127-AG70 | 2000 | Final Action | 04/00/2000 | Advanced Air Bags |
| UA-ECON-FINAL-000022 | 2127-AH95 | 2000 | Final Action | 04/00/2000 | Light Truck Fuel Economy Standards for Model Year 2002 |
| UA-ECON-FINAL-000023 | 2502-AG40 | 2000 | Final Action | 04/00/2000 | RESPA: Disclosure of Fees Paid to Retail Lenders (Brokers) (FR-3780) |
| UA-ECON-FINAL-000027 | 0938-AI57 | 2000 | Final Action | 05/00/2000 | Security and Electronic Signature Standards (HCFA-0049-F) / Security Signature Standards (HCFA-0049-F) |
| UA-ECON-FINAL-000029 | 0584-AC63 | 2000 | Final Action | 06/00/2000 | Food Stamp Provisions of the Balanced Budget Act of 1997 |

## Missingness Risks

- UA timetable records are embedded JSON within a per-RIN/per-vintage flat table; no separate source timetable-row file was packaged.
- Generic final labels, interim final rules, temporary final rules, notices, corrections, delays, stays, and withdrawals are audited rather than included.
- Old FR-linked baselines can contain RIN aliases and document-level evidence that a pure UA-core pass intentionally has not resolved yet.
- RegStats counts use presidential years and external determinations; this step uses UA final-action calendar years.
