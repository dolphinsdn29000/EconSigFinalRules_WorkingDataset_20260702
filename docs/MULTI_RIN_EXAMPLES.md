# Multi-RIN Rule-Level Examples

Source file: `/Volumes/OWC Envoy Pro FX/EconSigFinalRules_WorkingDataset_20260702/data/release_current/econ_sig_final_rules_rule_level_2000_2024_cfr_audited.csv`

Rows with more than one RIN in `econ_rin_list`: **95**

This file is a small audit sample for understanding why a collapsed rule row can have multiple RINs.

## Example 1: Food Stamp Program: Recipient Claim Establishment and Collection Standards

- Rule group key: `2000-07-06__FRDOC_00-16775`
- Presidential year: `2000`
- Representative FR doc key: `2000-07-06__FRDOC_00-16775`
- Representative FR date: `2000-07-06`
- Representative FR action: `Final rule.`
- Representative agency header: `DEPARTMENT OF AGRICULTURE`
- Representative CFR: `7 CFR Parts 272 and 273`
- Econ RIN list: `0584-AB88 | 0584-AB89`
- Source UA econ RIN: `True`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2000-07-06__FRDOC_00-16775` | `2000-07-06` | Food Stamp Program: Recipient Claim Establishment and Collection Standards | action: `Final rule.` | source: `2000-07-06__FRDOC_00-16775:UA+REGSTATS_OIRA`

### UA records connected through RINs

#### `0584-AB88`

- `ua_priority_category`: Other Significant | Economically Significant
- `ua_rule_title`: Food Stamp Program: Food Stamp Recipient Claim Establishment and Collection Standards
- `ua_agency_name`: Food and Nutrition Service
- `ua_parent_agency_name`: Department of Agriculture
- `ua_rule_stage`: Proposed Rule Stage | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 07/00/1996 | 10/00/1996 | 08/00/1996 | 10/00/1996 | 12/00/1997 | 02/00/1998 | 05/00/1998 | 10/00/1998 | 09/00/1998 | 12/00/1998 | 09/00/1999 | 12/00/1999 | 09/00/1999 | 03/00/2000 | 12/00/1999 | 06/00/2000 | 01/00/2000 | 01/00/2001 | 04/00/2000 | 04/00/2001 | 07/06/2000 | 08/01/2001
- `ua_nprm_dates`: 12/00/1995 | 02/00/1996 | 04/00/1996 | 06/00/1996 | 04/00/1997 | 07/00/1997 | 07/00/1997 | 09/00/1997 | 12/00/1997 | 02/00/1998 | 05/00/1998 | 07/00/1998 | 05/28/1998 | 08/26/1998
- `ua_timetable_summary`: NPRM:12/00/1995 | NPRM Comment Period End:02/00/1996 | Final Action:07/00/1996 | Final Action Effective:10/00/1996 | NPRM:04/00/1996 | NPRM Comment Period End:06/00/1996 | Final Action:08/00/1996 | Final Action Effective:10/00/1996 | NPRM:04/00/1997 | NPRM Comment Period End:07/00/1997 | Final Action:12/00/1997 | Final Action Effective:02/00/1998 | NPRM:07/00/1997 | NPRM Comment Period End:09/00/1997 | Final Action:05/00/1998 | Final Action Effective:10/00/1998 | NPRM:12/00/1997 | NPRM Comment Period End:02/00/1998 | Final Action:09/00/1998 | Final Action Effective:12/00/1998 | NPRM:05/00/1998 | NPRM Comment Period End:07/00/1998 | Final Action:09/00/1999 | Final Action Effective:12/00/1999 | NPRM:05/28/1998:63 FR 29303 | NPRM Comment Period End:08/26/1998 | Final Action:09/00/1999 | Final Action Effective:03/00/2000 | NPRM:05/28/1998:63 FR 29303 | NPRM Comment Period End:08/26/1998 | Final Action:12/00/1999 | Final Action Effective:06/00/2000 | NPRM:05/28/1998:63 FR 29303 | NPRM Comment Period End:08/26/1998 | Final Action:01/00/2000 | Final Action Effective:01/00/2001 | NPRM:05/28/1998:63 FR 29303 | NPRM Comment Period End:08/26/1998 | Final Action:04/00/2000 | Final Action Effective:04/00/2001 | NPRM:05/28/1998:63 FR 29303 | NPRM Comment Period End:08/26/1998 | Final Action:07/06/2000:65 FR 41752 | Final Action Effective:08/01/2001
- `ua_vintage`: 199510 | 199604 | 199610 | 199704 | 199710 | 199804 | 199810 | 199904 | 199910 | 200004 | 200010

#### `0584-AB89`

- `ua_priority_category`: Other Significant
- `ua_rule_title`: Collecting Food Stamp Recipient Claims From Federal Income Tax Refunds and Federal Salaries
- `ua_agency_name`: Food and Nutrition Service
- `ua_parent_agency_name`: Department of Agriculture
- `ua_rule_stage`: Completed Actions
- `ua_final_rule_dates`: 09/01/1995
- `ua_nprm_dates`: 06/28/1995 | 07/28/1995
- `ua_timetable_summary`: NPRM:06/28/1995:60 FR 33612 | NPRM Comment Period End:07/28/1995 | Final Action:09/01/1995:60 FR 45990
- `ua_vintage`: 199510

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 2: Amendments to Summary Plan Description Regulations

- Rule group key: `2000-11-21__FRDOC_00-29765`
- Presidential year: `2000`
- Representative FR doc key: `2000-11-21__FRDOC_00-29765`
- Representative FR date: `2000-11-21`
- Representative FR action: `Final rule.`
- Representative agency header: `DEPARTMENT OF LABOR`
- Representative CFR: `29 CFR Part 2520`
- Econ RIN list: `1210-AA55 | 1210-AA69`
- Source UA econ RIN: `False`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2000-11-21__FRDOC_00-29765` | `2000-11-21` | Amendments to Summary Plan Description Regulations | action: `Final rule.` | source: `2000-11-21__FRDOC_00-29765:REGSTATS_OIRA`

### UA records connected through RINs

#### `1210-AA55`

- `ua_priority_category`: Other Significant
- `ua_rule_title`: Amendment of Summary Plan Description and Related ERISA Regulations to Implement Statutory Changes in the Health Insurance Portability and Accountability Act of 1996 | Amendment of Summary Plan Description and Related ERISA Regulations To Implement Statutory Changes in the Health Insurance Portability and Accountability Act of 1996
- `ua_agency_name`: Employee Benefits Security Administration
- `ua_parent_agency_name`: Department of Labor
- `ua_rule_stage`: Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 04/00/1997 | 04/08/1997 | 05/31/1997 | 06/01/1997 | 04/08/1997 | 05/31/1997 | 06/01/1997 | 06/00/1998 | 04/08/1997 | 05/31/1997 | 06/01/1997 | 09/00/1998 | 04/08/1997 | 05/31/1997 | 06/01/1997 | 09/09/1998 | 11/09/1998 | 06/00/1999 | 04/08/1997 | 05/31/1997 | 06/01/1997 | 09/09/1998 | 11/09/1998 | 09/00/1999 | 04/08/1997 | 05/31/1997 | 06/01/1997 | 09/09/1998 | 11/09/1998 | 12/00/1999 | 04/08/1997 | 05/31/1997 | 06/01/1997 | 09/09/1998 | 11/09/1998 | 11/00/2000 | 04/08/1997 | 05/31/1997 | 06/01/1997 | 09/09/1998 | 11/09/1998 | 11/21/2000 | 01/20/2001
- `ua_timetable_summary`: Interim Final Rule:04/00/1997 | Interim Final Rule:04/08/1997:62 FR 16979 | Interim Final Rule Comment Period End:05/31/1997 | Interim Final Rule Effective:06/01/1997 | Interim Final Rule:04/08/1997:62 FR 16979 | Interim Final Rule Comment Period End:05/31/1997 | Interim Final Rule Effective:06/01/1997 | Final Action:06/00/1998 | Interim Final Rule:04/08/1997:62 FR 16979 | Interim Final Rule Comment Period End:05/31/1997 | Interim Final Rule Effective:06/01/1997 | Final Action:09/00/1998 | Interim Final Rule:04/08/1997:62 FR 16979 | Interim Final Rule Comment Period End:05/31/1997 | Interim Final Rule Effective:06/01/1997 | Interim Final Rule Second:09/09/1998:63 FR 48372 | Interim Final Rule Effective:11/09/1998 | Comment Period End:11/09/1998 | Final Action:06/00/1999 | Interim Final Rule:04/08/1997:62 FR 16979 | Interim Final Rule Comment Period End:05/31/1997 | Interim Final Rule Effective:06/01/1997 | Interim Final Rule Second:09/09/1998:63 FR 48372 | Interim Final Rule Effective:11/09/1998 | Comment Period End:11/09/1998 | Final Action:09/00/1999 | Interim Final Rule:04/08/1997:62 FR 16979 | Interim Final Rule Comment Period End:05/31/1997 | Interim Final Rule Effective:06/01/1997 | Interim Final Rule Second:09/09/1998:63 FR 48372 | Interim Final Rule Effective:11/09/1998 | Comment Period End:11/09/1998 | Final Action:12/00/1999 | Interim Final Rule:04/08/1997:62 FR 16979 | Interim Final Rule Comment Period End:05/31/1997 | Interim Final Rule Effective:06/01/1997 | Second Interim Final Rule:09/09/1998:63 FR 48372 | Interim Final Rule Effective:11/09/1998 | Comment Period End:11/09/1998 | Final Action:11/00/2000 | Interim Final Rule:04/08/1997:62 FR 16979 | Interim Final Rule Comment Period End:05/31/1997 | Interim Final Rule Effective:06/01/1997 | Second Interim Final Rule:09/09/1998:63 FR 48372 | Interim Final Rule Effective:11/09/1998 | Comment Period End:11/09/1998 | Final Action:11/21/2000:65 FR 70226 | Final Action Effective:01/20/2001
- `ua_vintage`: 199610 | 199704 | 199710 | 199804 | 199810 | 199904 | 199910 | 200004 | 200010 | 200104

#### `1210-AA69`

- `ua_priority_category`: Substantive, Nonsignificant | Other Significant
- `ua_rule_title`: Amendments to Summary Plan Description Regulations
- `ua_agency_name`: Employee Benefits Security Administration
- `ua_parent_agency_name`: Department of Labor
- `ua_rule_stage`: Prerule Stage | Proposed Rule Stage | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 03/00/1999 | 09/00/1999 | 12/00/1999 | 11/00/2000 | 11/21/2000 | 01/20/2001
- `ua_nprm_dates`: 08/00/1998 | 09/09/1998 | 11/09/1998
- `ua_timetable_summary`: ANPRM:08/00/1998 | NPRM:09/09/1998:63 FR 48376 | NPRM Comment Period End:11/09/1998 | Final Action:03/00/1999 | NPRM:09/09/1998:63 FR 48376 | NPRM Comment Period End:11/09/1998 | Final Action:09/00/1999 | NPRM:09/09/1998:63 FR 48376 | NPRM Comment Period End:11/09/1998 | Final Action:12/00/1999 | NPRM:09/09/1998:63 FR 48376 | NPRM Comment Period End:11/09/1998 | Final Action:11/00/2000 | NPRM:09/09/1998:63 FR 48376 | NPRM Comment Period End:11/09/1998 | Final Action:11/21/2000:65 FR 70226 | Final Action Effective:01/20/2001
- `ua_vintage`: 199804 | 199810 | 199904 | 199910 | 200004 | 200010 | 200104

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 3: State Child Health; Implementing Regulations for the State Children's Health Insurance Program

- Rule group key: `2001-01-11__FRDOC_01-607`
- Presidential year: `2000`
- Representative FR doc key: `2001-01-11__FRDOC_01-607`
- Representative FR date: `2001-01-11`
- Representative FR action: `Final rule.`
- Representative agency header: `DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Representative CFR: `42 CFR Parts 431, 433, 435, 436, and 457`
- Econ RIN list: `0938-AI28 | 0938-AJ75`
- Source UA econ RIN: `True`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2001-01-11__FRDOC_01-607` | `2001-01-11` | State Child Health; Implementing Regulations for the State Children's Health Insurance Program | action: `Final rule.` | source: `2001-01-11__FRDOC_01-607:UA+REGSTATS_OIRA`

### UA records connected through RINs

#### `0938-AI28`

- `ua_priority_category`: Economically Significant
- `ua_rule_title`: Children's Health Insurance: Program Implementations; State Plan Approval; State Payment; Coordination With State Medicaid Program | Children's Health Insurance: Program Implementations; State Plan Approval; State Payment; Coordination With State Medicaid Program (HCFA-2006-P) | Children's Health Insurance: Program Implementation; State Plan Approval; State Payment; Coordination With State Medicaid Program (HCFA-2006-P) | State Child Health; Implementing Regulations for the State Children's Health Insurance Program (HCFA-2006-P) | State Child Health; Implementing Regulations for the State Children's Health Insurance Program (HCFA-2006-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Proposed Rule Stage | Long-Term Actions | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 09/00/2000
- `ua_nprm_dates`: 12/00/1999 | 06/00/1999 | 11/00/1999 | 11/08/1999 | 01/07/2000
- `ua_timetable_summary`: NPRM Allotments and State Payment Policies:12/00/1999 | NPRM Allotments and State Payment Policies:06/00/1999 | NPRM:11/00/1999 | NPRM:11/08/1999:64 FR 60882 | NPRM Comment Period End:01/07/2000 | Final Action:09/00/2000 | NPRM:11/08/1999:64 FR 60882 | NPRM Comment Period End:01/07/2000 | Duplicate of RIN 0938-AJ75:08/10/2000
- `ua_vintage`: 199710 | 199804 | 199810 | 199904 | 199910 | 200004 | 200010

#### `0938-AJ75`

- `ua_priority_category`: Economically Significant
- `ua_rule_title`: The Children's Health Insurance Program: Implementing the Balanced Budget Act of 1997 (HCFA-2006-P) | The Children's Health Insurance Program: Implementing the Balanced Budget Act of 1997 (HCFA-2006-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 06/00/2000 | 09/00/2000 | 12/00/2000 | 01/11/2001
- `ua_nprm_dates`: 11/08/1999 | 11/08/1999 | 01/07/2000
- `ua_timetable_summary`: NPRM:11/08/1999:64 FR 60881 | Final Rule:06/00/2000 | NPRM:11/08/1999:64 FR 60881 | NPRM Comment Period End:01/07/2000 | Final Action:09/00/2000 | NPRM:11/08/1999:64 FR 60881 | NPRM Comment Period End:01/07/2000 | Final Action:12/00/2000 | NPRM:11/08/1999:64 FR 60881 | NPRM Comment Period End:01/07/2000 | Final Action:01/11/2001:66 FR 2490
- `ua_vintage`: 199910 | 200004 | 200010 | 200104

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 4: Medicaid Program; Change in Application of Federal Financial Participation Limits

- Rule group key: `2001-01-11__FRDOC_01-666`
- Presidential year: `2000`
- Representative FR doc key: `2001-01-11__FRDOC_01-666`
- Representative FR date: `2001-01-11`
- Representative FR action: `Final rule.`
- Representative agency header: `DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Representative CFR: `42 CFR Part 435`
- Econ RIN list: `0938-AJ96 | 0938-AK22`
- Source UA econ RIN: `True`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2001-01-11__FRDOC_01-666` | `2001-01-11` | Medicaid Program; Change in Application of Federal Financial Participation Limits | action: `Final rule.` | source: `2001-01-11__FRDOC_01-666:UA+REGSTATS_OIRA`

### UA records connected through RINs

#### `0938-AJ96`

- `ua_priority_category`: Economically Significant | Other Significant
- `ua_rule_title`: Use of Restraint and Seclusion in Residential Treatment Facilities Providing Inpatient Psychiatric Services to Individuals Under Age 21 (HCFA-2065-IFC) | Use of Restraint and Seclusion in Residential Treatment Facilities Providing Inpatient Psychiatric Services to Individuals Under Age 21 (HCFA-2065-F) | Use of Restraint and Seclusion in Residential Treatment Facilities Providing Inpatient Psychiatric Services to Individuals Under Age 21 (CMS-2065-F) | Use of Restraints and Seclusion in Residential Treatment Facilities Providing Inpatient Psychiatric Services to Individuals Under Age 21 (CMS-2065-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Long-Term Actions | Completed Actions | Final Rule Stage
- `ua_final_rule_dates`: To Be Determined | 01/11/2001 | 03/12/2001 | 01/22/2001 | 03/23/2001 | 03/23/2001 | 05/22/2001 | 07/23/2001 | 01/22/2001 | 03/23/2001 | 03/23/2001 | 05/22/2001 | 07/23/2001 | To Be Determined | 01/22/2001 | 03/23/2001 | 03/23/2001 | 05/22/2001 | 07/23/2001 | 06/00/2003 | 01/22/2001 | 03/23/2001 | 03/23/2001 | 05/22/2001 | 07/23/2001 | 09/00/2003 | 01/22/2001 | 03/23/2001 | 03/23/2001 | 05/22/2001 | 07/23/2001 | 09/00/2004 | 01/22/2001 | 03/23/2001 | 03/23/2001 | 05/22/2001 | 07/23/2001 | 04/00/2005 | 01/22/2001 | 03/23/2001 | 03/23/2001 | 05/22/2001 | 07/23/2001 | 12/00/2006 | 01/22/2001 | 03/23/2001 | 03/23/2001 | 05/22/2001 | 07/23/2001 | 09/00/2006 | 01/22/2001 | 03/23/2001 | 03/23/2001 | 05/22/2001 | 07/23/2001 | 10/00/2006 | 01/22/2001 | 03/23/2001 | 03/23/2001 | 05/22/2001 | 07/23/2001 | 05/00/2007
- `ua_timetable_summary`: Interim Final Rule:To Be Determined | Final Rule:01/11/2001:66 FR 2316 | Final Rule Effective:03/12/2001 | 60-Day Delay of Effective Date To 05/11/2001:03/12/2001:66 FR 14343 | Interim Final Rule:01/22/2001:66 FR 7148 | Interim Final Rule Comment Period End:03/23/2001 | Interim Final Rule Effective:03/23/2001 | 60-Day Delay of Effective Date To 05/22/2001:03/21/2001:66 FR 15800 | Interim Final Rule Amendment with Clarification:05/22/2001:66 FR 28110 | Interim Final Rule Comment Period End:07/23/2001 | Next Action Undetermined | Interim Final Rule:01/22/2001:66 FR 7148 | Interim Final Rule Comment Period End:03/23/2001 | Interim Final Rule Effective:03/23/2001 | 60-Day Delay of Effective Date To 05/22/2001:03/21/2001:66 FR 15800 | Interim Final Rule Amendment with Clarification:05/22/2001:66 FR 28110 | Interim Final Rule Comment Period End:07/23/2001 | Final Action:To Be Determined | Interim Final Rule:01/22/2001:66 FR 7148 | 60-Day Delay of Effective Date To 05/22/2001:03/21/2001:66 FR 15800 | Interim Final Rule Comment Period End:03/23/2001 | Interim Final Rule Effective:03/23/2001 | Interim Final Rule Amendment with Clarification:05/22/2001:66 FR 28110 | Interim Final Rule Comment Period End:07/23/2001 | Final Action:06/00/2003 | Interim Final Rule:01/22/2001:66 FR 7148 | 60-Day Delay of Effective Date To 05/22/2001:03/21/2001:66 FR 15800 | Interim Final Rule Comment Period End:03/23/2001 | Interim Final Rule Effective:03/23/2001 | Interim Final Rule Amendment with Clarification:05/22/2001:66 FR 28110 | Interim Final Rule Comment Period End:07/23/2001 | Final Action:09/00/2003 | Interim Final Rule:01/22/2001:66 FR 7148 | 60-Day Delay of Effective Date To 05/22/2001:03/21/2001:66 FR 15800 | Interim Final Rule Comment Period End:03/23/2001 | Interim Final Rule Effective:03/23/2001 | Interim Final Rule Amendment with Clarification:05/22/2001:66 FR 28110 | Interim Final Rule Comment Period End:07/23/2001 | Final Action:09/00/2004 | Interim Final Rule:01/22/2001:66 FR 7148 | 60-Day Delay of Effective Date To 05/22/2001:03/21/2001:66 FR 15800 | Interim Final Rule Comment Period End:03/23/2001 | Interim Final Rule Effective:03/23/2001 | Interim Final Rule Amendment with Clarification:05/22/2001:66 FR 28110 | Interim Final Rule Comment Period End:07/23/2001 | Final Action:04/00/2005 | Interim Final Rule:01/22/2001:66 FR 7148 | 60-Day Delay of Effective Date To 05/22/2001:03/21/2001:66 FR 15800 | Interim Final Rule Comment Period End:03/23/2001 | Interim Final Rule Effective:03/23/2001 | Interim Final Rule Amendment with Clarification:05/22/2001:66 FR 28110 | Interim Final Rule Comment Period End:07/23/2001 | Final Action:12/00/2006 | Interim Final Rule:01/22/2001:66 FR 7148 | 60-Day Delay of Effective Date To 05/22/2001:03/21/2001:66 FR 15800 | Interim Final Rule Comment Period End:03/23/2001 | Interim Final Rule Effective:03/23/2001 | Interim Final Rule Amendment with Clarification:05/22/2001:66 FR 28110 | Interim Final Rule Comment Period End:07/23/2001 | Final Action:09/00/2006 | Interim Final Rule:01/22/2001:66 FR 7148 | 60-Day Delay of Effective Date To 05/22/2001:03/21/2001:66 FR 15800 | Interim Final Rule Comment Period End:03/23/2001 | Interim Final Rule Effective:03/23/2001 | Interim Final Rule Amendment with Clarification:05/22/2001:66 FR 28110 | Interim Final Rule Comment Period End:07/23/2001 | Final Action:10/00/2006 | Interim Final Rule:01/22/2001:66 FR 7148 | 60-Day Delay of Effective Date To 05/22/2001:03/21/2001:66 FR 15800 | Interim Final Rule Comment Period End:03/23/2001 | Interim Final Rule Effective:03/23/2001 | Interim Final Rule Amendment with Clarification:05/22/2001:66 FR 28110 | Interim Final Rule Comment Period End:07/23/2001 | Final Action:05/00/2007
- `ua_vintage`: 200004 | 200010 | 200104 | 200110 | 200204 | 200210 | 200304 | 200310 | 200404 | 200410 | 200504 | 200510

#### `0938-AK22`

- `ua_priority_category`: Other Significant
- `ua_rule_title`: Application of Federal Financial Participation Limits (HCFA-2086-P) | Application of Federal Financial Participation Limits (HCFA-2086-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Long-Term Actions | Completed Actions
- `ua_final_rule_dates`: 01/11/2001
- `ua_nprm_dates`: 10/31/2000
- `ua_timetable_summary`: Next Action Undetermined | NPRM:10/31/2000:65 FR 64919 | Final Action:01/11/2001:66 FR 2316
- `ua_vintage`: 200010 | 200104

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 5: Medicare Program; Changes to the Hospital Inpatient Prospective Payment Systems and Rates and Costs of Graduate Medical Education: Fiscal Year 2002 Rates; Provisions of the Balanced Budget Refinement Act of 1999; and Provisions of the Medicare, Medicaid, and SCHIP Benefits Improvement and Protection Act of 2000

- Rule group key: `2001-08-01__FRDOC_01-18868`
- Presidential year: `2001`
- Representative FR doc key: `2001-08-01__FRDOC_01-18868`
- Representative FR date: `2001-08-01`
- Representative FR action: `Final rules.`
- Representative agency header: `DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Representative CFR: `42 CFR Parts 405, 410, 412, 413, 482, 485, and 486`
- Econ RIN list: `0938-AK20 | 0938-AK73 | 0938-AK74`
- Source UA econ RIN: `True`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2001-08-01__FRDOC_01-18868` | `2001-08-01` | Medicare Program; Changes to the Hospital Inpatient Prospective Payment Systems and Rates and Costs of Graduate Medical Education: Fiscal Year 2002 Rates; Provisions of the Balanced Budget Refinement Act of 1999; and Provisions of the Medicare, Medicaid, and SCHIP Benefits Improvement and Protection Act of 2000 | action: `Final rules.` | source: `2001-08-01__FRDOC_01-18868:UA+REGSTATS_OIRA`

### UA records connected through RINs

#### `0938-AK20`

- `ua_priority_category`: Other Significant
- `ua_rule_title`: Providers of the Balanced Budget and Refinement Act; Hospital Inpatient Payments, Rates and Costs of Graduate Medical Education (HCFA-1131-IFC) | Provisions of the Balanced Budget and Refinement Act of 1999; Hospital Inpatient Payments and Rates and Costs of Graduate Medical Education (HCFA-1131-IFC) | Provisions of the Balanced Budget and Refinement Act of 1999; Hospital Inpatient Payments and Rates and Costs of Graduate Medical Education (CMS-1131-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Long-Term Actions | Completed Actions
- `ua_final_rule_dates`: 08/01/2000 | 08/01/2000 | 08/31/2000 | 08/01/2000 | 08/01/2000 | 08/31/2000 | 08/01/2001 | 10/01/2001
- `ua_timetable_summary`: Interim Final Rule:08/01/2000:65 FR 47026 | Interim Final Rule Effective:08/01/2000 | Interim Final Rule Comment Period End:08/31/2000 | Next Action Undetermined | Interim Final Rule:08/01/2000:65 FR 47026 | Interim Final Rule Effective:08/01/2000 | Interim Final Rule Comment Period End:08/31/2000 | Final Action:08/01/2001:66 FR 39828 | Final Action Effective:10/01/2001
- `ua_vintage`: 200010 | 200104 | 200110

#### `0938-AK73`

- `ua_priority_category`: Economically Significant
- `ua_rule_title`: Changes to the Hospital Inpatients Prospective Payment System for Fiscal Year 2002 Rates (HCFA-1158-P) | Changes to the Hospital Inpatients Prospective Payment System for Fiscal Year 2002 Rates (CMS-1158-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Long-Term Actions | Completed Actions
- `ua_final_rule_dates`: 08/01/2001 | 10/01/2001
- `ua_nprm_dates`: 05/04/2001 | 07/03/2001
- `ua_timetable_summary`: Next Action Undetermined | NPRM:05/04/2001:66 FR 22646 | NPRM Comment Period End:07/03/2001 | Final Action:08/01/2001:66 FR 39828 | Final Action Effective:10/01/2001
- `ua_vintage`: 200104 | 200110

#### `0938-AK74`

- `ua_priority_category`: Other Significant | Economically Significant
- `ua_rule_title`: Changes to Inpatient BIPA for Fiscal Year 2001 (HCFA-1178-IFC) | Changes to Inpatient BIPA for Fiscal Year 2001 (CMS-1178-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Long-Term Actions | Completed Actions
- `ua_final_rule_dates`: 06/13/2001 | 06/13/2001 | 07/13/2001 | 08/01/2001 | 10/01/2001
- `ua_timetable_summary`: Next Action Undetermined | Interim Final Rule:06/13/2001:66 FR 32172 | Interim Final Rule Effective:06/13/2001 | Interim Final Rule Comment Period End:07/13/2001 | Final Action:08/01/2001:66 FR 39828 | Final Action Effective:10/01/2001
- `ua_vintage`: 200104 | 200110

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 6: Methods for Radiation Dose Reconstruction Under the Energy Employees Occupational Illness Compensation Program Act of 2000; Final Rule

- Rule group key: `2002-05-02__FRDOC_02-10764`
- Presidential year: `2002`
- Representative FR doc key: `2002-05-02__FRDOC_02-10763`
- Representative FR date: `2002-05-02`
- Representative FR action: `Final rule.`
- Representative agency header: `DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Representative CFR: `42 CFR Part 82`
- Econ RIN list: `0920-AA05 | 0920-ZA00 | 0920-ZA01`
- Source UA econ RIN: `False`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `2`

### Related Federal Register documents

- `2002-05-02__FRDOC_02-10763` | `2002-05-02` | Methods for Radiation Dose Reconstruction Under the Energy Employees Occupational Illness Compensation Program Act of 2000; Final Rule | action: `Final rule.` | source: `2002-05-02__FRDOC_02-10763:REGSTATS_OIRA`
- `2002-05-02__FRDOC_02-10764` | `` | Guidelines for Determining the Probability of Causation Under the Energy Employees Occupational Illness Compensation Program Act of 2000; Final Rule | action: `` | source: `2002-05-02__FRDOC_02-10764:REGSTATS_OIRA`

### UA records connected through RINs

#### `0920-AA05`

- `ua_priority_category`: Other Significant
- `ua_rule_title`: Methods for Estimating Radiation Dose and Guidelines for Assessing Probability of Cancer for Energy Employees Occupational Illness Compensation Program
- `ua_agency_name`: Centers for Disease Control and Prevention
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Proposed Rule Stage | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 04/00/2002 | 05/02/2002
- `ua_nprm_dates`: 05/00/2001 | 12/00/2001
- `ua_timetable_summary`: NPRM:05/00/2001 | NPRM:12/00/2001 | Final Rule:04/00/2002 | Final Rule:05/02/2002:67 FR 22296
- `ua_vintage`: 200104 | 200110 | 200204 | 200210

#### `0920-ZA00`

- No UA rows found for this RIN in `ua_all_flat_rin_norm.csv.gz`.

#### `0920-ZA01`

- No UA rows found for this RIN in `ua_all_flat_rin_norm.csv.gz`.

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 7: Claims Under the Radiation Exposure Compensation Act Amendments of 2000; Technical Amendments

- Rule group key: `2002-08-07__FRDOC_02-19221`
- Presidential year: `2002`
- Representative FR doc key: `2002-08-07__FRDOC_02-19221`
- Representative FR date: `2002-08-07`
- Representative FR action: `Final rule.`
- Representative agency header: `DEPARTMENT OF JUSTICE`
- Representative CFR: `28 CFR Part 79`
- Econ RIN list: `1105-AA57 | 1105-AA75`
- Source UA econ RIN: `False`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2002-08-07__FRDOC_02-19221` | `2002-08-07` | Claims Under the Radiation Exposure Compensation Act Amendments of 2000; Technical Amendments | action: `Final rule.` | source: `2002-08-07__FRDOC_02-19221:REGSTATS_OIRA`

### UA records connected through RINs

#### `1105-AA57`

- No UA rows found for this RIN in `ua_all_flat_rin_norm.csv.gz`.

#### `1105-AA75`

- `ua_priority_category`: Other Significant
- `ua_rule_title`: Claims Under the Radiation Exposure Compensation Act Amendments of 2000: Technical Amendments; Expansion of Coverage to Uranium Mill Workers and Ore Transporters | Claims Under the Radiation Exposure Compensation Act Amendments of 2000: Technical Amendments; Expansion of Coverage to Uranium Millers and Ore Transporters; Expansion of Coverage for Uranium Miners | Claims Under the Radiation Exposure Compensation Act Amendments of 2000; Amendments Contained in the Department of Justice Appropriations Authorization Act of 2002
- `ua_agency_name`: Legal Activities
- `ua_parent_agency_name`: Department of Justice
- `ua_rule_stage`: Proposed Rule Stage | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 12/00/2003 | 03/23/2004 | 04/22/2004
- `ua_timetable_summary`: Final Action:12/00/2003 | Final Action:03/23/2004:69 FR 13628 | Final Action Effective:04/22/2004
- `ua_vintage`: 200010 | 200104 | 200110 | 200204 | 200210 | 200304 | 200310 | 200404

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 8: Medicare Program; Medicare-Endorsed Prescription Drug Card Assistance Initiative

- Rule group key: `2002-09-04__FRDOC_02-22316`
- Presidential year: `2002`
- Representative FR doc key: `2002-09-04__FRDOC_02-22316`
- Representative FR date: `2002-09-04`
- Representative FR action: `Final rule.`
- Representative agency header: `DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Representative CFR: `42 CFR Part 403`
- Econ RIN list: `0938-AL25 | 0938-AL28`
- Source UA econ RIN: `False`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2002-09-04__FRDOC_02-22316` | `2002-09-04` | Medicare Program; Medicare-Endorsed Prescription Drug Card Assistance Initiative | action: `Final rule.` | source: `2002-09-04__FRDOC_02-22316:REGSTATS_OIRA`

### UA records connected through RINs

#### `0938-AL25`

- No UA rows found for this RIN in `ua_all_flat_rin_norm.csv.gz`.

#### `0938-AL28`

- `ua_priority_category`: Economically Significant
- `ua_rule_title`: Initiative to Endorse Prescription Drug Discount Programs (CMS-4027-P) | Medicare Program; Medicare-Endorsed Prescription Drug Discount Card Assistance Initiative (CMS-4027-P) | Medicare Program; Medicare-Endorsed Prescription Drug Discount Card Assistance Initiative (CMS-4027-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Proposed Rule Stage | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 06/00/2002 | 09/04/2002
- `ua_nprm_dates`: 12/00/2001 | 03/06/2002 | 05/26/2002 | 03/06/2002
- `ua_timetable_summary`: NPRM:12/00/2001 | NPRM:03/06/2002:67 FR 10262 | NPRM Comment Period End:05/26/2002 | Final Rule:06/00/2002 | Proposed Rule:03/06/2002:67 FR 10262 | Comment Period End:05/26/2002 | Final Rule:09/04/2002:67 FR 56618
- `ua_vintage`: 200110 | 200204 | 200210

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 9: Medicare Program; Changes to the Hospital Outpatient Prospective Payment System and Calendar Year 2003 Payment Rates; and Changes to Payment Suspension for Unfiled Cost Reports

- Rule group key: `2002-11-01__FRDOC_02-27548`
- Presidential year: `2002`
- Representative FR doc key: `2002-11-01__FRDOC_02-27548`
- Representative FR date: `2002-11-01`
- Representative FR action: `Final rule with comment period.`
- Representative agency header: `DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Representative CFR: `42 CFR Parts 405 and 419`
- Econ RIN list: `0938-AK59 | 0938-AL19`
- Source UA econ RIN: `False`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2002-11-01__FRDOC_02-27548` | `2002-11-01` | Medicare Program; Changes to the Hospital Outpatient Prospective Payment System and Calendar Year 2003 Payment Rates; and Changes to Payment Suspension for Unfiled Cost Reports | action: `Final rule with comment period.` | source: `2002-11-01__FRDOC_02-27548:REGSTATS_OIRA`

### UA records connected through RINs

#### `0938-AK59`

- `ua_priority_category`: Other Significant
- `ua_rule_title`: Revisions to the Prospective Payment System for Hospital Outpatient Services Mandated by BIPA (HCFA-1179-IFC) | Prospective Payment System for Hospital Outpatient Services: Criteria for Establishing New Pass-Through Categories for Medical Devices (CMS-1179-IFC)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Long-Term Actions | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 11/02/2001 | 09/00/2002 | 11/02/2001
- `ua_timetable_summary`: Next Action Undetermined | Interim Final Rule with Comment Period:11/02/2001:66 FR 55850 | Final Rule:09/00/2002 | Interim Final Rule with Comment Period:11/02/2001:66 FR 55850
- `ua_vintage`: 200104 | 200110 | 200204

#### `0938-AL19`

- `ua_priority_category`: Other Significant
- `ua_rule_title`: Hospital Outpatient Prospective Payment System for Calendar Year 2003 (CMS-1206-P) | Changes to the Hospital Outpatient Prospective Payment System and Calendar Year 2003 Payment Rates (CMS-1206-P) | Changes to the Hospital Outpatient Prospective Payment System and Calendar Year 2003 Payment Rates (CMS-1206-F) | Changes to the Hospital Outpatient Prospective Payment System and Calendar Year 2003 Payment Rates; Changes to Payment Suspension for Unfiled Cost Reports; Correction to Final Rule (CMS-1206-CN2)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Proposed Rule Stage | Final Rule Stage | Long-Term Actions | Completed Actions
- `ua_final_rule_dates`: 10/00/2002 | 11/00/2002 | 11/01/2002
- `ua_nprm_dates`: 05/00/2002 | 06/00/2002 | 08/09/2002
- `ua_timetable_summary`: NPRM:05/00/2002 | Final Action:10/00/2002 | NPRM with Comment Period:06/00/2002 | Notice:03/18/2002:67 FR 11969 | Proposed Rule:08/09/2002:67 FR 52092 | Comment Period End:10/07/2002 | Final Action:11/00/2002 | Notice:03/18/2002:67 FR 11969 | Proposed Rule:08/09/2002:67 FR 52092 | Comment Period End:10/07/2002 | Final Action:11/01/2002:67 FR 66718 | Correction Notice:11/15/2002:67 FR 69146 | Correction Notice:02/10/2003:68 FR 6636 | Next Action Undetermined | Notice:03/18/2002:67 FR 11969 | Proposed Rule:08/09/2002:67 FR 52092 | Comment Period End:10/07/2002 | Final Action:11/01/2002:67 FR 66718 | Correction Notice:10/01/2003:67 FR 69146 | Correction Notice:02/10/2003:68 FR 6636
- `ua_vintage`: 200110 | 200204 | 200210 | 200304 | 200310

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 10: Medicare Program; Changes to the Hospital Outpatient Prospective Payment System and Calendar Year 2004 Payment Rates

- Rule group key: `2003-11-07__FRDOC_03-27791`
- Presidential year: `2003`
- Representative FR doc key: `2003-11-07__FRDOC_03-27791`
- Representative FR date: `2003-11-07`
- Representative FR action: `Final rule with comment period.`
- Representative agency header: `DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Representative CFR: `42 CFR Parts 410 and 419`
- Econ RIN list: `0938-AL19 | 0938-AL91`
- Source UA econ RIN: `False`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2003-11-07__FRDOC_03-27791` | `2003-11-07` | Medicare Program; Changes to the Hospital Outpatient Prospective Payment System and Calendar Year 2004 Payment Rates | action: `Final rule with comment period.` | source: `2003-11-07__FRDOC_03-27791:REGSTATS_OIRA`

### UA records connected through RINs

#### `0938-AL19`

- `ua_priority_category`: Other Significant
- `ua_rule_title`: Hospital Outpatient Prospective Payment System for Calendar Year 2003 (CMS-1206-P) | Changes to the Hospital Outpatient Prospective Payment System and Calendar Year 2003 Payment Rates (CMS-1206-P) | Changes to the Hospital Outpatient Prospective Payment System and Calendar Year 2003 Payment Rates (CMS-1206-F) | Changes to the Hospital Outpatient Prospective Payment System and Calendar Year 2003 Payment Rates; Changes to Payment Suspension for Unfiled Cost Reports; Correction to Final Rule (CMS-1206-CN2)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Proposed Rule Stage | Final Rule Stage | Long-Term Actions | Completed Actions
- `ua_final_rule_dates`: 10/00/2002 | 11/00/2002 | 11/01/2002
- `ua_nprm_dates`: 05/00/2002 | 06/00/2002 | 08/09/2002
- `ua_timetable_summary`: NPRM:05/00/2002 | Final Action:10/00/2002 | NPRM with Comment Period:06/00/2002 | Notice:03/18/2002:67 FR 11969 | Proposed Rule:08/09/2002:67 FR 52092 | Comment Period End:10/07/2002 | Final Action:11/00/2002 | Notice:03/18/2002:67 FR 11969 | Proposed Rule:08/09/2002:67 FR 52092 | Comment Period End:10/07/2002 | Final Action:11/01/2002:67 FR 66718 | Correction Notice:11/15/2002:67 FR 69146 | Correction Notice:02/10/2003:68 FR 6636 | Next Action Undetermined | Notice:03/18/2002:67 FR 11969 | Proposed Rule:08/09/2002:67 FR 52092 | Comment Period End:10/07/2002 | Final Action:11/01/2002:67 FR 66718 | Correction Notice:10/01/2003:67 FR 69146 | Correction Notice:02/10/2003:68 FR 6636
- `ua_vintage`: 200110 | 200204 | 200210 | 200304 | 200310

#### `0938-AL91`

- `ua_priority_category`: Other Significant
- `ua_rule_title`: Changes to the Hospital Outpatient Prospective Payment System and Calendar Year 2004 Payment Rates (CMS-1471-P) | Changes to the Hospital Outpatient Prospective Payment System and Calendar Year 2004 Payment Rates (CMS-1471-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Proposed Rule Stage | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 12/00/2003 | 11/07/2003
- `ua_nprm_dates`: 06/00/2002 | 06/00/2003 | 08/12/2003
- `ua_timetable_summary`: NPRM:06/00/2002 | NPRM:06/00/2003 | NPRM:08/12/2003:68 FR 47966 | Final Action:12/00/2003 | NPRM:08/12/2003:68 FR 47966 | Final Action:11/07/2003:68 FR 63398
- `ua_vintage`: 200204 | 200210 | 200304 | 200310 | 200404

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 11: Required Advance Electronic Presentation of Cargo Information

- Rule group key: `2003-12-05__FRDOC_03-29798`
- Presidential year: `2003`
- Representative FR doc key: `2003-12-05__FRDOC_03-29798`
- Representative FR date: `2003-12-05`
- Representative FR action: `Final rule.`
- Representative agency header: `DEPARTMENT OF HOMELAND SECURITY`
- Representative CFR: `19 CFR Parts 4, 103, 113, 122, 123, 178 and 192`
- Econ RIN list: `1515-AD33 | 1651-AA49`
- Source UA econ RIN: `True`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2003-12-05__FRDOC_03-29798` | `2003-12-05` | Required Advance Electronic Presentation of Cargo Information | action: `Final rule.` | source: `2003-12-05__FRDOC_03-29798:UA+REGSTATS_OIRA`

### UA records connected through RINs

#### `1515-AD33`

- No UA rows found for this RIN in `ua_all_flat_rin_norm.csv.gz`.

#### `1651-AA49`

- `ua_priority_category`: Economically Significant
- `ua_rule_title`: Required Advance Electronic Presentation of Cargo Information
- `ua_agency_name`: Bureau of Customs and Border Protection
- `ua_parent_agency_name`: Department of Homeland Security
- `ua_rule_stage`: Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 12/00/2003 | 12/05/2003
- `ua_nprm_dates`: 07/23/2003 | 08/22/2003
- `ua_timetable_summary`: NPRM:07/23/2003:68 FR 43574 | NPRM Comment Period End:08/22/2003 | Final Action:12/00/2003 | NPRM:07/23/2003:68 FR 43574 | NPRM Comment Period End:08/22/2003 | Final Action:12/05/2003:68 FR 68140
- `ua_vintage`: 200310 | 200404

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 12: Salvage and Marine Firefighting Requirements; Vessel Response Plans for Oil

- Rule group key: `2004-01-23__FRDOC_04-1440`
- Presidential year: `2003`
- Representative FR doc key: `2004-01-23__FRDOC_04-1440`
- Representative FR date: `2004-01-23`
- Representative FR action: `Final rule; partial suspension of regulation.`
- Representative agency header: `DEPARTMENT OF HOMELAND SECURITY`
- Representative CFR: `33 CFR Part 155`
- Econ RIN list: `1625-AA19 | 2115-AF60`
- Source UA econ RIN: `True`
- Source RegStats/OIRA linked: `False`
- Related FR doc count: `1`

### Related Federal Register documents

- `2004-01-23__FRDOC_04-1440` | `2004-01-23` | Salvage and Marine Firefighting Requirements; Vessel Response Plans for Oil | action: `Final rule; partial suspension of regulation.` | source: `2004-01-23__FRDOC_04-1440:UA`

### UA records connected through RINs

#### `1625-AA19`

- `ua_priority_category`: Economically Significant | Substantive, Nonsignificant
- `ua_rule_title`: Salvage and Marine Firefighting Requirements; Vessel Response Plans for Oil (USCG-1998-3417)
- `ua_agency_name`: U.S. Coast Guard
- `ua_parent_agency_name`: Department of Homeland Security
- `ua_rule_stage`: Long-Term Actions | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 02/12/1998 | 01/17/2001 | 02/12/1998 | 01/17/2001 | 01/23/2004 | 02/12/1998 | 01/17/2001 | 01/23/2004 | 02/09/2007 | 02/12/1998 | 01/17/2001 | 01/23/2004 | 02/09/2007 | 12/00/2008 | 02/12/1998 | 01/17/2001 | 01/23/2004 | 02/09/2007 | 12/31/2008 | 01/30/2009 | 02/12/2009
- `ua_nprm_dates`: 05/10/2002 | 08/07/2002 | 10/18/2002
- `ua_timetable_summary`: Final Rule - Partial Suspension:02/12/1998:63 FR 7069 | Final Rule - Partial Suspension:01/17/2001:66 FR 3876 | NPRM:05/10/2002:67 FR 31868 | Public Meeting 7/9/02, 7/17/02, 7/25/02:06/12/2002:67 FR 40254 | Public Meeting 9/26/02:08/07/2002:67 FR 51159 | NPRM Comment Period Extended:08/07/2002:67 FR 51159 | NPRM Comment Period End:10/18/2002 | Next Action Undetermined | Final Rule - Partial Suspension:02/12/1998:63 FR 7069 | Final Rule - Partial Suspension:01/17/2001:66 FR 3876 | NPRM:05/10/2002:67 FR 31868 | Public Meeting 7/9/02, 7/17/02, 7/25/02:06/12/2002:67 FR 40254 | Public Meeting 9/26/02:08/07/2002:67 FR 51159 | NPRM Comment Period Extended:08/07/2002:67 FR 51159 | NPRM Comment Period End:10/18/2002 | Next Action Undetermined:To Be Determined | Final Rule - Partial Suspension:02/12/1998:63 FR 7069 | Final Rule - Partial Suspension:01/17/2001:66 FR 3876 | NPRM:05/10/2002:67 FR 31868 | Public Meeting 7/9/02, 7/17/02, 7/25/02:06/12/2002:67 FR 40254 | Public Meeting 9/26/02:08/07/2002:67 FR 51159 | NPRM Comment Period Extended:08/07/2002:67 FR 51159 | NPRM Comment Period End:10/18/2002 | Final Rule - Partial Suspension:01/23/2004:69 FR 3236 | Next Action Undetermined:To Be Determined | Final Rule - Partial Suspension:02/12/1998:63 FR 7069 | Final Rule - Partial Suspension:01/17/2001:66 FR 3876 | NPRM:05/10/2002:67 FR 31868 | Public Meeting 7/9/02, 7/17/02, 7/25/02:06/12/2002:67 FR 40254 | Public Meeting 9/26/02:08/07/2002:67 FR 51159 | NPRM Comment Period Extended:08/07/2002:67 FR 51159 | NPRM Comment Period End:10/18/2002 | Final Rule - Partial Suspension:01/23/2004:69 FR 3236 | Notice of Availability & Request for Comment:01/03/2006:71 FR 125 | Next Action Undetermined:To Be Determined | Final Rule - Partial Suspension:02/12/1998:63 FR 7069 | Final Rule - Partial Suspension:01/17/2001:66 FR 3876 | NPRM:05/10/2002:67 FR 31868 | Public Meeting 7/9/02, 7/17/02, 7/25/02:06/12/2002:67 FR 40254 | Public Meeting 9/26/02:08/07/2002:67 FR 51159 | NPRM Comment Period Extended:08/07/2002:67 FR 51159 | NPRM Comment Period End:10/18/2002 | Final Rule - Partial Suspension:01/23/2004:69 FR 3236 | Notice of Availability & Request for Comment:01/03/2006:71 FR 125 | Final Rule - Partial Suspension:02/09/2007:72 FR 6168 | Next Action Undetermined:To Be Determined | Final Rule - Partial Suspension:02/12/1998:63 FR 7069 | Final Rule - Partial Suspension:01/17/2001:66 FR 3876 | NPRM:05/10/2002:67 FR 31868 | Public Meeting 7/9/02, 7/17/02, 7/25/02:06/12/2002:67 FR 40254 | Public Meeting 9/26/02:08/07/2002:67 FR 51159 | NPRM Comment Period Extended:08/07/2002:67 FR 51159 | NPRM Comment Period End:10/18/2002 | Final Rule - Partial Suspension:01/23/2004:69 FR 3236 | Notice of Availability & Request for Comment:01/03/2006:71 FR 125 | Final Rule - Partial Suspension:02/09/2007:72 FR 6168 | Final Action:12/00/2008 | Final Rule--Partial Suspension:02/12/1998:63 FR 7069 | Final Rule--Partial Suspension:01/17/2001:66 FR 3876 | NPRM:05/10/2002:67 FR 31868 | Public Meeting 7/9/02, 7/17/02, 7/25/02:06/12/2002:67 FR 40254 | Public Meeting 9/26/02:08/07/2002:67 FR 51159 | NPRM Comment Period Extended:08/07/2002:67 FR 51159 | NPRM Comment Period End:10/18/2002 | Final Rule--Partial Suspension:01/23/2004:69 FR 3236 | Notice of Availability & Request for Comment:01/03/2006:71 FR 125 | Final Rule--Partial Suspension:02/09/2007:72 FR 6168 | Final Action:12/00/2008 | Final Rule--Partial Suspension:02/12/1998:63 FR 7069 | Final Rule--Partial Suspension:01/17/2001:66 FR 3876 | NPRM:05/10/2002:67 FR 31868 | Public Meeting 7/9/02, 7/17/02, 7/25/02:06/12/2002:67 FR 40254 | Public Meeting 9/26/02:08/07/2002:67 FR 51159 | NPRM Comment Period Extended:08/07/2002:67 FR 51159 | NPRM Comment Period End:10/18/2002 | Final Rule--Partial Suspension:01/23/2004:69 FR 3236 | Notice of Availability & Request for Comment:01/03/2006:71 FR 125 | Final Rule--Partial Suspension:02/09/2007:72 FR 6168 | Final Rule:12/00/2008 | Final Rule--Partial Suspension:02/12/1998:63 FR 7069 | Final Rule--Partial Suspension:01/17/2001:66 FR 3876 | NPRM:05/10/2002:67 FR 31868 | Public Meeting 7/9/02, 7/17/02, 7/25/02:06/12/2002:67 FR 40254 | Public Meeting 9/26/02:08/07/2002:67 FR 51159 | NPRM Comment Period Extended:08/07/2002:67 FR 51159 | NPRM Comment Period End:10/18/2002 | Final Rule--Partial Suspension:01/23/2004:69 FR 3236 | Notice of Availability & Request for Comment:01/03/2006:71 FR 125 | Final Rule--Partial Suspension:02/09/2007:72 FR 6168 | Final Rule:12/31/2008:73 FR 80618 | Final Rule Effective:01/30/2009 | Final Rule Effective:02/12/2009
- `ua_vintage`: 200304 | 200310 | 200404 | 200410 | 200504 | 200510 | 200604 | 200610 | 200704 | 200710 | 200804 | 200810

#### `2115-AF60`

- `ua_priority_category`: Substantive, Nonsignificant | Other Significant | Economically Significant
- `ua_rule_title`: Salvage and Firefighting Equipment; Vessel Response Plans (USCG-98-3417) | Salvage and Firefighting Equipment; Vessel Response Plans (USCG-1998-3417) | Salvage and Marine Firefighting Requirement; Vessel Response Plans for Oil (USCG-1998-3417) | Salvage and Marine Firefighting Requirements; Vessel Response Plans for Oil (USCG-1998-3417)
- `ua_agency_name`: U.S. Coast Guard
- `ua_parent_agency_name`: Department of Transportation
- `ua_rule_stage`: Final Rule Stage | Long-Term Actions | Proposed Rule Stage | Completed Actions
- `ua_final_rule_dates`: 04/00/1998 | 02/12/1998 | 02/18/1998 | 02/18/1998 | 01/17/2001 | 02/12/1998 | 01/17/2001 | 02/12/1998 | 01/17/2001 | 12/00/2003
- `ua_nprm_dates`: 09/00/1999 | 09/00/2000 | 12/00/2000 | 09/00/2001 | 02/00/2002 | 12/00/2002 | 05/10/2002 | 08/07/2002 | 10/18/2002
- `ua_timetable_summary`: Final Rule: Partial Suspension:04/00/1998 | Final Rule: Partial Suspension:02/12/1998:63 FR 7069 | Final Rule: Partial Suspension:02/12/1998:63 FR 7069 | NPRM:09/00/1999 | Final Rule:Partial Suspension:02/18/1998:63 FR 7069 | NPRM:09/00/2000 | Final Rule - Partial Suspension:02/18/1998:63 FR 7069 | NPRM:12/00/2000 | Final Rule - Partial Suspension:02/18/1998:63 FR 7069 | Final Rule - Partial Suspension:01/17/2001:66 FR 3876 | NPRM:09/00/2001 | Final Rule - Partial Suspension:02/12/1998:63 FR 7069 | Final Rule - Partial Suspension:01/17/2001:66 FR 3876 | NPRM:02/00/2002 | Final Rule - Partial Suspension:02/12/1998:63 FR 7069 | Final Rule - Partial Suspension:01/17/2001:66 FR 3876 | NPRM:12/00/2002 | Final Rule - Partial Suspension:02/12/1998:63 FR 7069 | Final Rule - Partial Suspension:01/17/2001:66 FR 3876 | NPRM:05/10/2002:67 FR 31868 | Public Meeting 7/9/02, 7/17/02, 7/25/02:06/12/2002:67 FR 40254 | Public Meeting 9/26/02:08/07/2002:67 FR 51159 | NPRM Comment Period Extended:08/07/2002:67 FR 51159 | NPRM Comment Period End:10/18/2002 | Final Rule:12/00/2003 | Final Rule - Partial Suspension:02/12/1998:63 FR 7069 | Final Rule - Partial Suspension:01/17/2001:66 FR 3876 | NPRM:05/10/2002:67 FR 31868 | Public Meeting 7/9/02, 7/17/02, 7/25/02:06/12/2002:67 FR 40254 | Public Meeting 9/26/02:08/07/2002:67 FR 51159 | NPRM Comment Period Extended:08/07/2002:67 FR 51159 | NPRM Comment Period End:10/18/2002 | Transferred to RIN 1625-AA19:02/05/2003
- `ua_vintage`: 199804 | 199810 | 199904 | 199910 | 200004 | 200010 | 200104 | 200110 | 200204 | 200210 | 200304

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 13: Final Rule Declaring Dietary Supplements Containing Ephedrine Alkaloids Adulterated Because They Present an Unreasonable Risk

- Rule group key: `2004-02-11__FRDOC_04-2912`
- Presidential year: `2004`
- Representative FR doc key: `2004-02-11__FRDOC_04-2912`
- Representative FR date: `2004-02-11`
- Representative FR action: `Final rule.`
- Representative agency header: `DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Representative CFR: `21 CFR Part 119`
- Econ RIN list: `0910-AA59 | 0910-AF19`
- Source UA econ RIN: `False`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2004-02-11__FRDOC_04-2912` | `2004-02-11` | Final Rule Declaring Dietary Supplements Containing Ephedrine Alkaloids Adulterated Because They Present an Unreasonable Risk | action: `Final rule.` | source: `2004-02-11__FRDOC_04-2912:REGSTATS_OIRA`

### UA records connected through RINs

#### `0910-AA59`

- `ua_priority_category`: Routine and Frequent | Other Significant
- `ua_rule_title`: Dietary Supplement Regulations in Response to DSHEA
- `ua_agency_name`: Food and Drug Administration
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Proposed Rule Stage | Long-Term Actions | Completed Actions
- `ua_final_rule_dates`: 06/05/1998
- `ua_nprm_dates`: To Be Determined
- `ua_timetable_summary`: NPRM:To Be Determined | Final Rule-Nutrient Labeling and Ingredient Labeling; Dietary Supplements:06/05/1998:63 FR 30615
- `ua_vintage`: 199510 | 199604 | 199610 | 199704 | 199710 | 199804 | 199810 | 199904 | 199910

#### `0910-AF19`

- No UA rows found for this RIN in `ua_all_flat_rin_norm.csv.gz`.

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 14: Final Regulations for Health Coverage Portability for Group Health Plans and Group Health Insurance Issuers Under HIPAA Titles I & IV

- Rule group key: `2004-12-30__FRDOC_04-28112`
- Presidential year: `2004`
- Representative FR doc key: `2004-12-30__FRDOC_04-28112`
- Representative FR date: `2004-12-30`
- Representative FR action: `Final regulation.`
- Representative agency header: `DEPARTMENT OF THE TREASURY | DEPARTMENT OF LABOR | DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Representative CFR: `26 CFR Parts 54 and 602 | 29 CFR Part 2590 | 45 CFR Parts 144 and 146`
- Econ RIN list: `0938-AL43 | 1210-AA54 | 1545-AX84`
- Source UA econ RIN: `True`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2004-12-30__FRDOC_04-28112` | `2004-12-30` | Final Regulations for Health Coverage Portability for Group Health Plans and Group Health Insurance Issuers Under HIPAA Titles I & IV | action: `Final regulation.` | source: `2004-12-30__FRDOC_04-28112:UA+REGSTATS_OIRA`

### UA records connected through RINs

#### `0938-AL43`

- `ua_priority_category`: Other Significant | Economically Significant
- `ua_rule_title`: Health Coverage Portability for Group Health Plans and Group Health Insurance Issuers (CMS-2151-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Long-Term Actions | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 04/08/1997 | 07/07/1997 | 07/07/1997 | 04/08/1997 | 07/07/1997 | 07/07/1997 | 05/00/2003 | 04/08/1997 | 07/07/1997 | 07/07/1997 | 09/00/2003 | 04/08/1997 | 07/07/1997 | 07/07/1997 | 05/00/2004 | 04/08/1997 | 07/07/1997 | 07/07/1997 | 12/00/2006 | 04/08/1997 | 07/07/1997 | 07/07/1997 | 11/00/2004 | 04/08/1997 | 07/07/1997 | 07/07/1997 | 12/30/2004
- `ua_timetable_summary`: Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Comment Period End:07/07/1997 | Interim Final Rule Effective:07/07/1997 | Next Action Undetermined | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Comment Period End:07/07/1997 | Interim Final Rule Effective:07/07/1997 | Final Action:05/00/2003 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Comment Period End:07/07/1997 | Interim Final Rule Effective:07/07/1997 | Final Action:09/00/2003 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Comment Period End:07/07/1997 | Interim Final Rule Effective:07/07/1997 | Final Action:05/00/2004 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Comment Period End:07/07/1997 | Interim Final Rule Effective:07/07/1997 | Final Action:12/00/2006 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Comment Period End:07/07/1997 | Interim Final Rule Effective:07/07/1997 | Final Action:11/00/2004 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Comment Period End:07/07/1997 | Interim Final Rule Effective:07/07/1997 | Final Action:12/30/2004:69 FR 78720
- `ua_vintage`: 200204 | 200210 | 200304 | 200310 | 200404 | 200410 | 200504

#### `1210-AA54`

- `ua_priority_category`: Other Significant | Economically Significant
- `ua_rule_title`: Regulations Implementing the Health Care Access, Portability and Renewability Provision of the Health Insurance Portability and Accountability Act of 1996 | Regulations Implementing the Health Care Access, Portability and Renewability Provisions of the Health Insurance Portability and Accountability Act of 1996 | Regulations Implementing the Health Care Access, Portability, and Renewability Provisions of the Health Insurance Portability and Accountability Act of 1996
- `ua_agency_name`: Employee Benefits Security Administration
- `ua_parent_agency_name`: Department of Labor
- `ua_rule_stage`: Final Rule Stage | Long-Term Actions | Completed Actions
- `ua_final_rule_dates`: 04/00/1997 | 04/08/1997 | 06/07/1997 | 07/07/1997 | 04/08/1997 | 06/07/1997 | 07/07/1997 | 12/00/1998 | 04/08/1997 | 06/07/1997 | 07/07/1997 | 12/00/1999 | 04/08/1997 | 06/07/1997 | 07/07/1997 | 06/00/1999 | 04/08/1997 | 06/07/1997 | 07/07/1997 | 03/00/2000 | 04/08/1997 | 06/07/1997 | 07/07/1997 | 07/00/2000 | 04/08/1997 | 06/07/1997 | 07/07/1997 | 09/00/2000 | 04/08/1997 | 06/07/1997 | 07/07/1997 | 07/00/2001 | 04/08/1997 | 06/07/1997 | 07/07/1997 | 12/00/2001 | 04/08/1997 | 06/07/1997 | 07/07/1997 | 01/00/2002 | 04/08/1997 | 06/07/1997 | 07/07/1997 | 08/00/2002
- `ua_nprm_dates`: 12/30/2004 | 03/30/2005
- `ua_timetable_summary`: Interim Final Rule:04/00/1997 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Effective:06/07/1997 | Interim Final Rule Comment Period End:07/07/1997 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Effective:06/07/1997 | Interim Final Rule Comment Period End:07/07/1997 | Final Action:12/00/1998 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Effective:06/07/1997 | Interim Final Rule Comment Period End:07/07/1997 | Final Action:12/00/1999 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Effective:06/07/1997 | Interim Final Rule Comment Period End:07/07/1997 | Final Action:06/00/1999 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Effective:06/07/1997 | Interim Final Rule Comment Period End:07/07/1997 | Final Rule:03/00/2000 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Effective:06/07/1997 | Interim Final Rule Comment Period End:07/07/1997 | Request for Information:10/25/1999:64 FR 57520 | Comment Period End:01/25/2000 | Final Rule:07/00/2000 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Effective:06/07/1997 | Interim Final Rule Comment Period End:07/07/1997 | Request for Information:10/25/1999:64 FR 57520 | Comment Period End:01/25/2000 | Final Rule:09/00/2000 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Effective:06/07/1997 | Interim Final Rule Comment Period End:07/07/1997 | Request for Information:10/25/1999:64 FR 57520 | Comment Period End:01/25/2000 | Final Rule:07/00/2001 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Effective:06/07/1997 | Interim Final Rule Comment Period End:07/07/1997 | Request for Information:10/25/1999:64 FR 57520 | Comment Period End:01/25/2000 | Final Rule:12/00/2001 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Effective:06/07/1997 | Interim Final Rule Comment Period End:07/07/1997 | Request for Information:10/25/1999:64 FR 57520 | Comment Period End:01/25/2000 | Final Rule:01/00/2002 | Interim Final Rule:04/08/1997:62 FR 16894 | Interim Final Rule Effective:06/07/1997 | Interim Final Rule Comment Period End:07/07/1997 | Request for Information:10/25/1999:64 FR 57520 | Comment Period End:01/25/2000 | Final Rule:08/00/2002
- `ua_vintage`: 199610 | 199704 | 199710 | 199804 | 199810 | 199904 | 199910 | 200004 | 200010 | 200104 | 200110 | 200204

#### `1545-AX84`

- `ua_priority_category`: Substantive, Nonsignificant
- `ua_rule_title`: HIPAA Portability
- `ua_agency_name`: Internal Revenue Service
- `ua_parent_agency_name`: Department of the Treasury
- `ua_rule_stage`: Final Rule Stage | Long-Term Actions | Completed Actions
- `ua_final_rule_dates`: 04/08/1997 | 10/00/2000 | 12/00/2000 | 12/00/2001 | 12/00/2003 | 09/00/2004 | 12/00/2004 | 12/30/2004
- `ua_nprm_dates`: 04/08/1997
- `ua_timetable_summary`: NPRM:04/08/1997:62 FR 16977 | Interim Final Rule:04/08/1997:62 FR 16977 | Final Action:10/00/2000 | NPRM:04/08/1997:62 FR 16977 | Final Action:12/00/2000 | NPRM:04/08/1997:62 FR 16977 | Final Action:12/00/2001 | NPRM:04/08/1997:62 FR 16977 | Final Action:12/00/2003 | NPRM:04/08/1997:62 FR 16977 | Final Action:09/00/2004 | NPRM:04/08/1997:62 FR 16977 | Final Action:12/00/2004 | NPRM:04/08/1997:62 FR 16977 | Final Action Completed by TD 9166:12/30/2004:69 FR 78720
- `ua_vintage`: 200004 | 200010 | 200104 | 200110 | 200204 | 200210 | 200304 | 200310 | 200404 | 200410 | 200504

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 15: Medicare Program; Revisions to Payment Policies Under the Physician Fee Schedule for Calendar Year 2006 and Certain Provisions Related to the Competitive Acquisition Program of Outpatient Drugs and Biologicals Under Part B

- Rule group key: `2005-11-21__FRDOC_05-22160`
- Presidential year: `2005`
- Representative FR doc key: `2005-11-21__FRDOC_05-22160`
- Representative FR date: `2005-11-21`
- Representative FR action: `Final rule with comment.`
- Representative agency header: `DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Representative CFR: `42 CFR Part 405, 410, 411, 413, 414, 424, and 426`
- Econ RIN list: `0938-AN58 | 0938-AN84`
- Source UA econ RIN: `True`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2005-11-21__FRDOC_05-22160` | `2005-11-21` | Medicare Program; Revisions to Payment Policies Under the Physician Fee Schedule for Calendar Year 2006 and Certain Provisions Related to the Competitive Acquisition Program of Outpatient Drugs and Biologicals Under Part B | action: `Final rule with comment.` | source: `2005-11-21__FRDOC_05-22160:UA+REGSTATS_OIRA`

### UA records connected through RINs

#### `0938-AN58`

- `ua_priority_category`: Economically Significant | Other Significant
- `ua_rule_title`: Medicare Part B Competitive Acquisition of Outpatient Drugs and Biologicals (CMS-1325-P) | Medicare Part B Competitive Acquisition of Outpatient Drugs and Biologicals (CMS-1325-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Proposed Rule Stage | Long-Term Actions | Completed Actions
- `ua_final_rule_dates`: 03/00/2008 | 07/06/2005 | 07/00/2008 | 07/06/2005 | 09/06/2005 | 11/21/2005 | 08/18/2006 | 10/02/2006 | 08/00/2009 | 07/06/2005 | 09/06/2005 | 11/21/2005 | 08/18/2006 | 10/02/2006 | 07/00/2008 | 07/06/2005 | 09/06/2005 | 11/21/2005 | 08/18/2006 | 10/02/2006
- `ua_nprm_dates`: 02/00/2005 | 03/04/2005
- `ua_timetable_summary`: NPRM:02/00/2005 | NPRM:03/04/2005:70 FR 10745 | Final Action:03/00/2008 | NPRM:03/04/2005:70 FR 10745 | Interim Final Rule:07/06/2005:70 FR 39022 | Final Action:07/00/2008 | NPRM:03/04/2005:70 FR 10745 | Interim Final Rule:07/06/2005:70 FR 39022 | Second Interim Final Rule:09/06/2005:70 FR 52930 | Third Interim Final Rule:11/21/2005:70 FR 70478 | Fourth Interim Final Rule:08/18/2006:71 FR 47870 | Fourth Interim Final Rule Comment Period End:10/02/2006 | Final Action:08/00/2009 | NPRM:03/04/2005:70 FR 10745 | Interim Final Rule:07/06/2005:70 FR 39022 | Second Interim Final Rule:09/06/2005:70 FR 52930 | Third Interim Final Rule:11/21/2005:70 FR 70478 | Fourth Interim Final Rule:08/18/2006:71 FR 47870 | Fourth Interim Final Rule Comment Period End:10/02/2006 | Final Action:07/00/2008 | NPRM:03/04/2005:70 FR 10745 | Interim Final Rule:07/06/2005:70 FR 39022 | Second Interim Final Rule:09/06/2005:70 FR 52930 | Third Interim Final Rule:11/21/2005:70 FR 70478 | Fourth Interim Final Rule:08/18/2006:71 FR 47870 | Fourth Interim Final Rule Comment Period End:10/02/2006 | Withdrawn:08/08/2007
- `ua_vintage`: 200410 | 200504 | 200510 | 200604 | 200610 | 200704 | 200710

#### `0938-AN84`

- `ua_priority_category`: Economically Significant
- `ua_rule_title`: Revisions to Payment Policies Under the Physician Fee Schedule for Calendar Year 2006 (CMS-1502-P) | Revisions to Payment Policies Under the Physician Fee Schedule for Calendar Year 2006 (CMS-1502-FC)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Proposed Rule Stage | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 11/00/2005 | 11/21/2005
- `ua_nprm_dates`: 07/00/2005 | 08/08/2005
- `ua_timetable_summary`: NPRM:07/00/2005 | NPRM:08/08/2005:70 FR 45763 | Final Action:11/00/2005 | NPRM:08/08/2005:70 FR 45763 | Final Rule:11/21/2005:70 FR 70116 | Comment Period End:01/03/2006
- `ua_vintage`: 200504 | 200510 | 200604

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 16: Documents Required for Travelers Departing From or Arriving in the United States at Air Ports-of-Entry From Within the Western Hemisphere

- Rule group key: `2006-11-24__FRDOC_06-9402`
- Presidential year: `2006`
- Representative FR doc key: `2006-11-24__FRDOC_06-9402`
- Representative FR date: `2006-11-24`
- Representative FR action: `Final rule.`
- Representative agency header: `DEPARTMENT OF HOMELAND SECURITY | DEPARTMENT OF STATE`
- Representative CFR: `8 CFR Parts 212 and 235 | 22 CFR Parts 41 and 53`
- Econ RIN list: `1400-AC10 | 1651-AA66`
- Source UA econ RIN: `True`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2006-11-24__FRDOC_06-9402` | `2006-11-24` | Documents Required for Travelers Departing From or Arriving in the United States at Air Ports-of-Entry From Within the Western Hemisphere | action: `Final rule.` | source: `2006-11-24__FRDOC_06-9402:UA+REGSTATS_OIRA`

### UA records connected through RINs

#### `1400-AC10`

- `ua_priority_category`: Other Significant
- `ua_rule_title`: Documents Required for Travel Within the Western Hemisphere
- `ua_agency_name`: Department of State
- `ua_rule_stage`: Proposed Rule Stage | Completed Actions
- `ua_nprm_dates`: 01/00/2006 | 04/00/2006
- `ua_timetable_summary`: NPRM:01/00/2006 | NPRM:04/00/2006 | Withdrawn:08/23/2006
- `ua_vintage`: 200510 | 200604 | 200610

#### `1651-AA66`

- `ua_priority_category`: Other Significant | Economically Significant
- `ua_rule_title`: Documents Required for Travel Within the Western Hemisphere | Documents Required for Travelers Departing From or Arriving in the United States at Air Ports-of-Entry From Within the Western Hemisphere
- `ua_agency_name`: Bureau of Customs and Border Protection
- `ua_parent_agency_name`: Department of Homeland Security
- `ua_rule_stage`: Prerule Stage | Proposed Rule Stage | Completed Actions
- `ua_final_rule_dates`: 11/24/2006 | 01/23/2007
- `ua_nprm_dates`: 09/01/2005 | 10/31/2005 | 02/00/2006 | 09/01/2005 | 10/31/2005 | 05/00/2006 | 09/01/2005 | 10/31/2005 | 08/11/2006 | 09/25/2006
- `ua_timetable_summary`: ANPRM:09/01/2005:70 FR 52037 | ANPRM Comment Period End:10/31/2005 | NPRM:02/00/2006 | ANPRM:09/01/2005:70 FR 52037 | ANPRM Comment Period End:10/31/2005 | NPRM:05/00/2006 | ANPRM:09/01/2005:70 FR 52037 | ANPRM Comment Period End:10/31/2005 | NPRM:08/11/2006:71 FR 46155 | NPRM Comment Period End:09/25/2006 | Final Action:11/24/2006:71 FR 68411 | Final Action Effective:01/23/2007
- `ua_vintage`: 200510 | 200604 | 200610

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 17: Medicare Program; Revisions to Payment Policies, Five-Year Review of Work Relative Value Units, Changes to the Practice Expense Methodology Under the Physician Fee Schedule, and Other Changes to Payment Under Part B; Revisions to the Payment Policies of Ambulance Services Under the Fee Schedule for Ambulance Services; and Ambulance Inflation Factor Update for CY 2007

- Rule group key: `2006-12-01__FRDOC_06-9086`
- Presidential year: `2006`
- Representative FR doc key: `2006-12-01__FRDOC_06-9086`
- Representative FR date: `2006-12-01`
- Representative FR action: `Final rule with comment period.`
- Representative agency header: `DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Representative CFR: `42 CFR Parts 405, 410, 411, 414, 415, and 424`
- Econ RIN list: `0938-AO11 | 0938-AO24`
- Source UA econ RIN: `True`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2006-12-01__FRDOC_06-9086` | `2006-12-01` | Medicare Program; Revisions to Payment Policies, Five-Year Review of Work Relative Value Units, Changes to the Practice Expense Methodology Under the Physician Fee Schedule, and Other Changes to Payment Under Part B; Revisions to the Payment Policies of Ambulance Services Under the Fee Schedule for Ambulance Services; and Ambulance Inflation Factor Update for CY 2007 | action: `Final rule with comment period.` | source: `2006-12-01__FRDOC_06-9086:UA+REGSTATS_OIRA`

### UA records connected through RINs

#### `0938-AO11`

- `ua_priority_category`: Substantive, Nonsignificant | Other Significant
- `ua_rule_title`: Revisions to Payment of Ambulance Services under Medicare (CMS-1317-P) | Revisions to the Payment Policies of Ambulance Services Under the Fee Schedule for Ambulance Services (CMS-1317-P) | Revisions to the Payment Policies of Ambulance Services Under the Fee Schedule for Ambulance Services (CMS-1317-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Proposed Rule Stage | Completed Actions
- `ua_nprm_dates`: 01/00/2006 | 06/00/2006 | 05/26/2006
- `ua_timetable_summary`: NPRM:01/00/2006 | NPRM:06/00/2006 | NPRM:05/26/2006:71 FR 30358 | Withdrawn:09/12/2006
- `ua_vintage`: 200510 | 200604 | 200610

#### `0938-AO24`

- `ua_priority_category`: Economically Significant
- `ua_rule_title`: Revisions to Payment Policies Under the Physician Fee Schedule for Calendar Year 2007 (CMS-1321-P) | Revisions to Payment Policies under the Physician Fee Schedule and Ambulance Fee Schedule for Calendar Year 2007 (CMS-1321-FC)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Proposed Rule Stage | Completed Actions
- `ua_final_rule_dates`: 12/01/2006 | 01/01/2007
- `ua_nprm_dates`: 07/00/2006 | 08/22/2006
- `ua_timetable_summary`: NPRM:07/00/2006 | NPRM:08/22/2006:71 FR 48982 | Final Action:12/01/2006:71 FR 69624 | Final Action Effective:01/01/2007
- `ua_vintage`: 200510 | 200604 | 200610

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 18: Risk-Based Capital Standards: Advanced Capital Adequacy Framework — Basel II

- Rule group key: `2007-12-07__FRDOC_07-5729`
- Presidential year: `2007`
- Representative FR doc key: `2007-12-07__FRDOC_07-5729`
- Representative FR date: `2007-12-07`
- Representative FR action: `Final rule.`
- Representative agency header: `DEPARTMENT OF THE TREASURY | FEDERAL RESERVE SYSTEM | FEDERAL DEPOSIT INSURANCE CORPORATION | DEPARTMENT OF THE TREASURY`
- Representative CFR: `12 CFR Part 3 | 12 CFR Parts 208 and 225 | 12 CFR Part 325 | 12 CFR Parts 559, 560, 563, and 567`
- Econ RIN list: `1550-AB56 | 1557-AC91 | 3064-AC73`
- Source UA econ RIN: `True`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2007-12-07__FRDOC_07-5729` | `2007-12-07` | Risk-Based Capital Standards: Advanced Capital Adequacy Framework — Basel II | action: `Final rule.` | source: `2007-12-07__FRDOC_07-5729:UA+REGSTATS_OIRA`

### UA records connected through RINs

#### `1550-AB56`

- `ua_priority_category`: Substantive, Nonsignificant | Economically Significant
- `ua_rule_title`: Risk-Based Capital Guidelines; Implementation of New Basel Capital Accord | Implementation of a Revised Basel Capital Accord (Basel II)
- `ua_agency_name`: Office of Thrift Supervision
- `ua_parent_agency_name`: Department of the Treasury
- `ua_rule_stage`: Prerule Stage | Proposed Rule Stage | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 06/00/2007 | 12/00/2007 | 12/07/2007 | 04/01/2008
- `ua_nprm_dates`: 08/04/2003 | 11/03/2003 | 08/04/2003 | 11/03/2003 | 12/00/2004 | 08/04/2003 | 11/03/2003 | 05/00/2005 | 08/04/2003 | 11/03/2003 | 06/00/2005 | 08/04/2003 | 11/03/2003 | 12/00/2005 | 08/04/2003 | 11/03/2003 | 04/00/2006 | 08/04/2003 | 11/03/2003 | 09/25/2006 | 01/23/2007 | 08/04/2003 | 11/03/2003 | 09/25/2006 | 01/23/2007 | 12/26/2006 | 03/26/2007
- `ua_timetable_summary`: ANPRM:08/04/2003:68 FR 45900 | ANPRM Comment Period End:11/03/2003 | ANPRM:08/04/2003:68 FR 45900 | ANPRM Comment Period End:11/03/2003 | NPRM:12/00/2004 | ANPRM:08/04/2003:68 FR 45900 | ANPRM Comment Period End:11/03/2003 | NPRM:05/00/2005 | ANPRM:08/04/2003:68 FR 45900 | ANPRM Comment Period End:11/03/2003 | NPRM:06/00/2005 | ANPRM:08/04/2003:68 FR 45900 | ANPRM Comment Period End:11/03/2003 | NPRM:12/00/2005 | ANPRM:08/04/2003:68 FR 45900 | ANPRM Comment Period End:11/03/2003 | NPRM:04/00/2006 | ANPRM:08/04/2003:68 FR 45900 | ANPRM Comment Period End:11/03/2003 | NPRM:09/25/2006:71 FR 55830 | NPRM Comment Period End:01/23/2007 | ANPRM:08/04/2003:68 FR 45900 | ANPRM Comment Period End:11/03/2003 | NPRM:09/25/2006:71 FR 55830 | NPRM Comment Period End:01/23/2007 | NPRM Comment Period Extended:12/26/2006:71 FR 77518 | NPRM Comment Period End:03/26/2007 | Final Rule:06/00/2007 | ANPRM:08/04/2003:68 FR 45900 | ANPRM Comment Period End:11/03/2003 | NPRM:09/25/2006:71 FR 55830 | NPRM Comment Period End:01/23/2007 | NPRM Comment Period Extended:12/26/2006:71 FR 77518 | NPRM Comment Period End:03/26/2007 | Final Rule:12/00/2007 | ANPRM:08/04/2003:68 FR 45900 | ANPRM Comment Period End:11/03/2003 | NPRM:09/25/2006:71 FR 55830 | NPRM Comment Period End:01/23/2007 | NPRM Comment Period Extended:12/26/2006:71 FR 77518 | NPRM Comment Period End:03/26/2007 | Final Action:12/07/2007:72 FR 69288 | Final Action Effective:04/01/2008
- `ua_vintage`: 200310 | 200404 | 200410 | 200504 | 200510 | 200604 | 200610 | 200704 | 200710 | 200804

#### `1557-AC91`

- `ua_priority_category`: Substantive, Nonsignificant | Economically Significant
- `ua_rule_title`: Implementation of a Revised Basel Capital Accord (Basel II)
- `ua_agency_name`: Comptroller of the Currency
- `ua_parent_agency_name`: Department of the Treasury
- `ua_rule_stage`: Proposed Rule Stage | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 06/00/2007 | 12/00/2007 | 12/07/2007 | 04/01/2008
- `ua_nprm_dates`: 12/00/2004 | 08/04/2003 | 08/00/2005 | 08/04/2003 | 06/00/2005 | 08/04/2003 | 02/00/2006 | 08/04/2003 | 05/00/2006 | 08/04/2003 | 09/25/2006 | 01/23/2007 | 08/04/2003 | 09/25/2006 | 01/23/2007 | 12/26/2006
- `ua_timetable_summary`: NPRM:12/00/2004 | ANPRM:08/04/2003:68 FR 45900 | NPRM:08/00/2005 | ANPRM:08/04/2003:68 FR 45900 | NPRM:06/00/2005 | ANPRM:08/04/2003:68 FR 45900 | NPRM:02/00/2006 | ANPRM:08/04/2003:68 FR 45900 | NPRM:05/00/2006 | ANPRM:08/04/2003:68 FR 45900 | NPRM:09/25/2006:71 FR 55830 | NPRM Comment Period End:01/23/2007 | ANPRM:08/04/2003:68 FR 45900 | NPRM:09/25/2006:71 FR 55830 | NPRM Comment Period End:01/23/2007 | NPRM Comment Period Extended From 01/23/2007 to 03/26/2007:12/26/2006:71 FR 77518 | Final Action:06/00/2007 | ANPRM:08/04/2003:68 FR 45900 | NPRM:09/25/2006:71 FR 55830 | NPRM Comment Period End:01/23/2007 | NPRM Comment Period Extended From 01/23/2007 to 03/26/2007:12/26/2006:71 FR 77518 | Final Action:12/00/2007 | ANPRM:08/04/2003:68 FR 45900 | NPRM:09/25/2006:71 FR 55830 | NPRM Comment Period End:01/23/2007 | NPRM Comment Period Extended From 01/23/2007 to 03/26/2007:12/26/2006:71 FR 77518 | Final Action:12/07/2007:72 FR 69288 | Final Action Effective:04/01/2008
- `ua_vintage`: 200404 | 200410 | 200504 | 200510 | 200604 | 200610 | 200704 | 200710 | 200804

#### `3064-AC73`

- `ua_priority_category`: Other Significant | Substantive, Nonsignificant
- `ua_rule_title`: Risk-Based Guidelines; Implementation of New Basel Capital Accord | Risk-Based Guidelines: Implementation of New Basel Capital Accord | Risk-Based Capital Standards: Implementation of New Basel Capital Accord
- `ua_agency_name`: Federal Deposit Insurance Corporation
- `ua_rule_stage`: Prerule Stage | Long-Term Actions | Proposed Rule Stage | Completed Actions
- `ua_final_rule_dates`: To Be Determined | 12/07/2007
- `ua_nprm_dates`: 08/04/2003 | 11/03/2003 | 08/04/2003 | To Be Determined | 08/04/2003 | 07/00/2005 | 08/04/2003 | 08/04/2003 | 09/25/2006 | 01/23/2007 | 08/04/2003 | 11/03/2003 | 09/25/2006 | 01/23/2007
- `ua_timetable_summary`: ANPRM:08/04/2003:68 FR 45900 | ANPRM Comment Period End:11/03/2003 | ANPRM:08/04/2003:68 FR 45900 | NPRM:To Be Determined | ANPRM:08/04/2003:68 FR 45900 | NPRM:07/00/2005 | ANPRM:08/04/2003:68 FR 45900 | To Be Determined:To Be Determined | ANPRM:08/04/2003:68 FR 45900 | NPRM:09/25/2006:71 FR 55830 | NPRM Comment Period End:01/23/2007 | ANPRM:08/04/2003:68 FR 45900 | NPRM:09/25/2006:71 FR 55830 | NPRM Comment Period End:01/23/2007 | Final Action:To Be Determined | ANPRM:08/04/2003:68 FR 45900 | ANPRM Comment Period End:11/03/2003 | NPRM:09/25/2006:71 FR 55830 | NPRM Comment Period End:01/23/2007 | Final Action:To Be Determined | ANPRM:08/04/2003:68 FR 45900 | ANPRM Comment Period End:11/03/2003 | NPRM:09/25/2006:71 FR 55830 | NPRM Comment Period End:01/23/2007 | Final Action:12/07/2007:72 FR 69437
- `ua_vintage`: 200310 | 200404 | 200410 | 200504 | 200510 | 200604 | 200610 | 200704 | 200710 | 200804

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 19: Medicare Program; Standards for E-Prescribing Under Medicare Part D and Identification of Backward Compatible Version of Adopted Standard for E-Prescribing and the Medicare Prescription Drug Program (Version 8.1)

- Rule group key: `2008-04-07__FRDOC_08-1094`
- Presidential year: `2008`
- Representative FR doc key: `2008-04-07__FRDOC_08-1094`
- Representative FR date: `2008-04-07`
- Representative FR action: `Final rule.`
- Representative agency header: `DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Representative CFR: `42 CFR Part 423`
- Econ RIN list: `0938-AO42 | 0938-AO66`
- Source UA econ RIN: `True`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2008-04-07__FRDOC_08-1094` | `2008-04-07` | Medicare Program; Standards for E-Prescribing Under Medicare Part D and Identification of Backward Compatible Version of Adopted Standard for E-Prescribing and the Medicare Prescription Drug Program (Version 8.1) | action: `Final rule.` | source: `2008-04-07__FRDOC_08-1094:UA+REGSTATS_OIRA`

### UA records connected through RINs

#### `0938-AO42`

- `ua_priority_category`: Info./Admin./Other | Other Significant
- `ua_rule_title`: Adoption of Standards for the E-Prescribing and the Medicare Prescription Drug Program (CMS-0018-N) | Identification of Backward Compatible Version of Adopted Standard for E-Prescribing and the Medicare Prescription Drug Program (Version 8.1) (CMS-0018-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Final Rule Stage | Long-Term Actions | Completed Actions
- `ua_final_rule_dates`: 06/00/2006 | 06/23/2006 | 06/00/2009 | 06/23/2006 | 08/22/2006 | 06/00/2009 | 06/23/2006 | 08/22/2006
- `ua_timetable_summary`: Final Action:06/00/2006 | Interim Final Rule:06/23/2006:71 FR 36020 | Final Action:06/00/2009 | Interim Final Rule:06/23/2006:71 FR 36020 | Interim Final Rule Comment Period End:08/22/2006 | Final Action:06/00/2009 | Interim Final Rule:06/23/2006:71 FR 36020 | Interim Final Rule Comment Period End:08/22/2006 | Withdrawn:07/23/2007
- `ua_vintage`: 200604 | 200610 | 200704 | 200710

#### `0938-AO66`

- `ua_priority_category`: Economically Significant | Other Significant
- `ua_rule_title`: Standards for E-Prescribing Under Medicare Part D (CMS-0016-P) | Standards for E-Prescribing Under Medicare Part D (CMS-0016-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Proposed Rule Stage | Completed Actions
- `ua_final_rule_dates`: 04/00/2008 | 04/07/2008 | 06/06/2008
- `ua_nprm_dates`: 06/00/2007 | 08/00/2007 | 11/16/2007 | 01/15/2008
- `ua_timetable_summary`: NPRM:06/00/2007 | NPRM:08/00/2007 | NPRM:11/16/2007:72 FR 64900 | NPRM Comment Period End:01/15/2008 | Final Action:04/00/2008 | NPRM:11/16/2007:72 FR 64900 | NPRM Comment Period End:01/15/2008 | Final Action:04/07/2008:73 FR 18918 | Final Action Effective:06/06/2008
- `ua_vintage`: 200610 | 200704 | 200710 | 200804

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

## Example 20: Medicare Program; Prospective Payment System for Long-Term Care Hospitals RY 2009: Annual Payment Rate Updates, Policy Changes, and Clarifications; and Electronic Submission of Cost Reports: Revision to Effective Date of Cost Reporting Period

- Rule group key: `2008-05-09__FRDOC_08-1219`
- Presidential year: `2008`
- Representative FR doc key: `2008-05-09__FRDOC_08-1219`
- Representative FR date: `2008-05-09`
- Representative FR action: `Final rule.`
- Representative agency header: `DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Representative CFR: `42 CFR Part 412`
- Econ RIN list: `0938-AN87 | 0938-AO94`
- Source UA econ RIN: `True`
- Source RegStats/OIRA linked: `True`
- Related FR doc count: `1`

### Related Federal Register documents

- `2008-05-09__FRDOC_08-1219` | `2008-05-09` | Medicare Program; Prospective Payment System for Long-Term Care Hospitals RY 2009: Annual Payment Rate Updates, Policy Changes, and Clarifications; and Electronic Submission of Cost Reports: Revision to Effective Date of Cost Reporting Period | action: `Final rule.` | source: `2008-05-09__FRDOC_08-1219:UA+REGSTATS_OIRA`

### UA records connected through RINs

#### `0938-AN87`

- `ua_priority_category`: Substantive, Nonsignificant
- `ua_rule_title`: Electronic Submission of Cost Reports: Revision to Cost Reporting Period (CMS-1199-IFC) | Electronic Submission of Cost Reports: Revision to Cost Reporting Period (CMS-1199-F) | Electronic Submission of Cost Reports (CMS-1199-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Final Rule Stage | Long-Term Actions | Completed Actions
- `ua_final_rule_dates`: 05/00/2005 | 05/27/2005 | 05/00/2008 | 05/27/2005
- `ua_timetable_summary`: Interim Final Rule Comment Period End:05/00/2005 | Interim Final Rule:05/27/2005:70 FR 30640 | Final Action:05/00/2008 | Interim Final Rule:05/27/2005:70 FR 30640 | Withdrawn:02/10/2006
- `ua_vintage`: 200504 | 200510 | 200604

#### `0938-AO94`

- `ua_priority_category`: Economically Significant
- `ua_rule_title`: Prospective Payment System for Long-Term Care Hospitals RY 2009: Annual Payment Rate Updates (CMS-1393-P) | Prospective Payment System for Long-Term Care Hospitals RY 2009: Annual Payment Rate Updates (CMS-1393-F)
- `ua_agency_name`: Centers for Medicare & Medicaid Services
- `ua_parent_agency_name`: Department of Health and Human Services
- `ua_rule_stage`: Proposed Rule Stage | Final Rule Stage | Completed Actions
- `ua_final_rule_dates`: 05/00/2008 | 05/09/2008
- `ua_nprm_dates`: 01/00/2008 | 01/29/2008 | 03/24/2008
- `ua_timetable_summary`: NPRM:01/00/2008 | NPRM:01/29/2008:73 FR 5342 | NPRM Comment Period End:03/24/2008 | Final Action:05/00/2008 | NPRM:01/29/2008:73 FR 5342 | NPRM Comment Period End:03/24/2008 | Final Action:05/09/2008:73 FR 26788
- `ua_vintage`: 200704 | 200710 | 200804 | 200810

### Initial audit interpretation

- Check whether the multiple RINs appear in the same FR document, across related FR documents, or as former/successor RINs.
- If the row is a joint agency rule or one FR document explicitly lists all RINs, it likely makes sense.
- If the row is connected only through a chain of related documents, it needs closer review.

