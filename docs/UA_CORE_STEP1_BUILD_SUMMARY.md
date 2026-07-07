# UA Core Step 1 Build Summary

This step builds only the Unified Agenda side of the conservative economic-prong final-action base. It does not match to Federal Register documents and does not build the final FR-document dataset.

## Source

- UA source: `source_inputs/ua_all_flat_rin_norm.csv.gz`
- Timetable source: embedded `ua_timetable_json` action/date/FR-citation lists.
- No separate more-granular UA timetable source file was present under `source_inputs/`.

## Counts

- Total UA rows read: 233,951
- Distinct RINs read: 44,284
- Legacy `Economically Significant` rows: 9,836
- `Section 3(f)(1) Significant` rows: 833
- Strict UA-core final-action candidates, 2000-2024: 3,614
- Distinct RINs in strict base: 1,603
- Strict base rows with explicit FR citation: 1,382
- Strict base rows with exact day-level parsed dates: 1,388

## Parser Rules

- Main inclusion requires the economic-prong priority label, `Final Rule Stage` or `Completed Actions`, a strict final-action/final-rule timetable label, and a final-action year from 2000 through 2024.
- Strict labels include `Final Action`, `Final Rule`, `Final Revision`, `Final Regulation(s)`, and `Direct Final Rule`.
- Effective-date and compliance-date labels are audit-only and are not included in the strict base.
- NPRM/ANPRM/proposed actions, notices, corrections, technical amendments, delays, stays, withdrawals, comment-period events, interim final rules, and temporary final rules stay out of the strict base and go to the excluded/uncertain table.
- Partial dates such as `08/00/2024` are used only for the year window; `final_action_date_parsed` is filled only for exact day-level dates.

## Counts By Year

| final_action_year | count |
| --- | --- |
| 2000 | 105 |
| 2001 | 85 |
| 2002 | 89 |
| 2003 | 90 |
| 2004 | 92 |
| 2005 | 90 |
| 2006 | 84 |
| 2007 | 119 |
| 2008 | 161 |
| 2009 | 135 |
| 2010 | 151 |
| 2011 | 159 |
| 2012 | 108 |
| 2013 | 153 |
| 2014 | 142 |
| 2015 | 171 |
| 2016 | 227 |
| 2017 | 79 |
| 2018 | 93 |
| 2019 | 122 |
| 2020 | 189 |
| 2021 | 202 |
| 2022 | 194 |
| 2023 | 259 |
| 2024 | 315 |

## Counts By Priority Label

| priority_label | count |
| --- | --- |
| Economically Significant | 3266 |
| Section 3(f)(1) Significant | 376 |

## Section 3(f)(1) Examples

Section 3(f)(1) rows are included for Tony review because EO 14094 changed the label during 2023-2024. Rows can still have earlier final-action dates when a later UA vintage carries older timetable history.

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

| rin_norm | final_action_year | ua_priority_category | ua_rule_title | final_action_label | final_action_date_raw |
| --- | --- | --- | --- | --- | --- |
| 3084-AB46 | 2017 | Section 3(f)(1) Significant | Premerger Notification Rules and Report Form | Final Rule (HSR Form Update) | 07/12/2017 |
| 3084-AB46 | 2018 | Section 3(f)(1) Significant | Premerger Notification Rules and Report Form | Final Rule (HSR Form Instructions Update) | 07/16/2018 |
| 3084-AB46 | 2019 | Section 3(f)(1) Significant | Premerger Notification Rules and Report Form | Final Rule (HSR Form Instructions Update) | 06/27/2019 |
| 0790-AK85 | 2020 | Economically Significant / Section 3(f)(1) Significant | National Industrial Security Program Operating Manual (NISPOM) | Final Action | 12/21/2020 |
| 0790-AK85 | 2021 | Economically Significant / Section 3(f)(1) Significant | National Industrial Security Program Operating Manual (NISPOM) | Final Rule Amendment | 08/19/2021 |
| 1205-AC00 | 2021 | Economically Significant / Section 3(f)(1) Significant | Strengthening Wage Protections for the Temporary and Permanent Employment of Certain Aliens in the United States | Final Rule | 01/14/2021 |
| 1205-AC00 | 2021 | Section 3(f)(1) Significant | Strengthening Wage Protections for the Temporary and Permanent Employment of Certain Aliens in the United States | Final Rule (Implementation of Court's Vacatur of Final Rule) | 12/13/2021 |
| 0625-AB21 | 2022 | Economically Significant / Section 3(f)(1) Significant | Procedures Covering Suspension of Liquidation, Duties and Estimated Duties in Accord with Presidential Proclamation 10414 / Procedures Covering Suspension of Liquidation, Duties an | Final Action | 09/16/2022 |
| 0570-AB07 | 2023 | Section 3(f)(1) Significant | B&I CARES Act Guaranteed Loan Program--Final Rule 7 CFR 4279 | Final Rule | 11/24/2023 |
| 0581-AE06 | 2023 | Section 3(f)(1) Significant | Organic Livestock and Poultry Standards (AMS-NOP-21-0073) | Final Rule | 11/02/2023 |
| 0605-AA51 | 2023 | Section 3(f)(1) Significant | Securing the Information and Communications Technology and Services Supply Chain | Final Action | 11/00/2023 |
| 0693-AB70 | 2023 | Section 3(f)(1) Significant | Preventing the Improper Use of CHIPS Act Funding | Final Action | 09/25/2023 |
| 0693-AB70 | 2023 | Section 3(f)(1) Significant | Preventing the Improper Use of CHIPS Act Funding | Final Rule Amendment | 12/28/2023 |
| 0910-AH99 | 2023 | Economically Significant / Section 3(f)(1) Significant | Medical Devices; Quality System Regulation Amendments | Final Rule | 12/00/2023 |
| 0938-AU00 | 2023 | Section 3(f)(1) Significant | Streamlining the Medicaid, CHIP, and BHP Application, Eligibility Determination, Enrollment, and Renewal Processes (CMS-2421) | 1st Final Action | 09/21/2023 |
| 0938-AU24 | 2023 | Section 3(f)(1) Significant | Treatment of Medicare Part C Days in the Calculation of a Hospital's Medicare Disproportionate Patient Percentage (CMS-1739) | Final Action | 06/09/2023 |
| 0938-AU24 | 2023 | Economically Significant / Section 3(f)(1) Significant | Treatment of Medicare Part C Days in the Calculation of a Hospital's Medicare Disproportionate Patient Percentage (CMS-1739) | Final Action | 08/00/2023 |
| 0938-AU75 | 2023 | Section 3(f)(1) Significant | Omnibus COVID-19 Health Care Staff Vaccination (CMS-3415) | Final Action | 06/05/2023 |
| 0938-AU97 | 2023 | Section 3(f)(1) Significant | HHS Notice of Benefit and Payment Parameters for 2024 (CMS-9899) | Final Action | 04/27/2023 |
| 0938-AV02 | 2023 | Section 3(f)(1) Significant | FY 2024 Skilled Nursing Facility (SNF) PPS and Consolidated Billing and Updates to the Value-Based Purchasing and Quality Reporting Programs (CMS-1779) | Final Action | 08/07/2023 |

## Included Examples

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
| UA-ECON-FINAL-000029 | 0584-AC63 | 2000 | Economically Significant | Food Stamp Provisions of the Balanced Budget Act of 1997 | Final Action |  |
| UA-ECON-FINAL-000016 | 0648-AM59 | 2000 | Economically Significant | Rule Governing the Take of Seven Threatened Evolutionarily Significant Units (ESUs) of West Coast Salmonids | Final Action |  |
| UA-ECON-FINAL-000002 | 0910-AE35 | 2000 | Economically Significant | HACCP for Juice | Final Action |  |
| UA-ECON-FINAL-000017 | 0910-AE35 | 2000 | Economically Significant | HACCP for Juice | Final Action |  |
| UA-ECON-FINAL-000048 | 0910-AE35 | 2000 | Economically Significant | HACCP for Juice | Final Action |  |
| UA-ECON-FINAL-000086 | 0910-AE35 | 2000 | Economically Significant | HACCP for Juice | Final Action |  |
| UA-ECON-FINAL-000049 | 0938-AI28 | 2000 | Economically Significant | State Child Health; Implementing Regulations for the State Children's Health Insurance Program (HCFA-2006-F) | Final Action |  |
| UA-ECON-FINAL-000006 | 0938-AI56 | 2000 | Economically Significant | Medicare Program; Prospective Payment System for Hospital Outpatient Services (HCFA-1005-F) | Final Action |  |
| UA-ECON-FINAL-000025 | 0938-AI56 | 2000 | Economically Significant | Prospective Payment System for Hospital Outpatient Services (HCFA-1005-F) | Final Action | 65 FR 18434 |
| UA-ECON-FINAL-000030 | 0938-AI56 | 2000 | Economically Significant | Medicare Program; Prospective Payment System for Hospital Outpatient Services (HCFA-1005-F) | Final Action |  |
| UA-ECON-FINAL-000087 | 0938-AI56 | 2000 | Economically Significant | Medicare Program; Prospective Payment System for Hospital Outpatient Services (HCFA-1005-F) | Final Action |  |
| UA-ECON-FINAL-000027 | 0938-AI57 | 2000 | Economically Significant | Security and Electronic Signature Standards (HCFA-0049-F) / Security Signature Standards (HCFA-0049-F) | Final Action |  |
| UA-ECON-FINAL-000012 | 0938-AI59 | 2000 | Economically Significant | National Standard Employer Identifier (HCFA-0047-F) | Final Action |  |
| UA-ECON-FINAL-000088 | 0938-AI59 | 2000 | Economically Significant | National Standard Employer Identifier (HCFA-0047-F) | Final Action |  |
| UA-ECON-FINAL-000089 | 0938-AI96 | 2000 | Economically Significant | Expanded Coverage for Diabetes Outpatient Self-Management Training Services (HCFA-3002-P) | Final Action |  |
| UA-ECON-FINAL-000105 | 0938-AI96 | 2000 | Economically Significant | Expanded Coverage for Diabetes Outpatient Self-Management Training Services (HCFA-3002-F) | Final Action | 65 FR 83130 |
| UA-ECON-FINAL-000031 | 0938-AJ75 | 2000 | Economically Significant | The Children's Health Insurance Program: Implementing the Balanced Budget Act of 1997 (HCFA-2006-P) | Final Rule |  |
| UA-ECON-FINAL-000050 | 0938-AJ75 | 2000 | Economically Significant | The Children's Health Insurance Program: Implementing the Balanced Budget Act of 1997 (HCFA-2006-F) | Final Action |  |
| UA-ECON-FINAL-000090 | 0938-AJ75 | 2000 | Economically Significant | The Children's Health Insurance Program: Implementing the Balanced Budget Act of 1997 (HCFA-2006-F) | Final Action |  |
| UA-ECON-FINAL-000039 | 0938-AJ93 | 2000 | Economically Significant | Prospective Payment System and Consolidated Billing for Skilled Nursing Facilities-Update (HCFA-1112-F) | Final Action | 65 FR 46770 |

## Main Limitations

- This is a UA-side event base, not a Federal Register document dataset.
- The parser is intentionally conservative; generic or ambiguous labels containing `final` are audited rather than included.
- A RIN can appear more than once when the UA timetable has multiple distinct final-action dates.
- FR document numbers are not available in the packaged UA timetable JSON and are left blank.
