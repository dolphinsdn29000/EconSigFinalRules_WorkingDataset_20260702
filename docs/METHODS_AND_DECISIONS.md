# Methods and Decisions

This note explains what the current pipeline is trying to do, why the choices
were made, and where the dataset still needs caution.

## Objective

The target object is:

```text
One row per economically significant final rule, linked to Federal Register and
Unified Agenda information.
```

Important limits:

- The target is not "all major rules."
- The target is not proposed rules.
- The target is not notices.
- The target is not every document associated with a RIN.
- A single rule may list multiple RINs.
- A single rule may have multiple related FR documents; the rule-level output
  collapses related documents into one row where possible.

## Evidence Sources

The package uses these compact inputs:

1. Parsed Federal Register final-rule documents.
2. Parsed Federal Register RIN explosion table.
3. Parsed Unified Agenda RIN-vintage table.
4. Strict OIRA/RegStats-to-FR linked file.
5. RegStats benchmark counts by presidential year.

The current release was built as a union of:

```text
UA priority category says economically significant / 3(f)(1)
OR external OIRA/RegStats linked evidence says economically significant / 3(f)(1)
```

That union is useful for auditing, but it means the current release is not a
pure UA+FR construction dataset.

## Why UA Priority Alone Is Too Narrow

The audit found 118 external econ-only final-rule documents from 2000-2024 that
were not found by a UA-priority-only construction.  The largest reason was:

```text
RIN exists in UA, but UA priority is not econ significant: 95 rows
```

The clearest example is RIN `0960-AB01`, the Social Security musculoskeletal
disability criteria final rule published on 2001-11-19.

For that rule:

```text
Raw Fall 2001 UA:
  PRIORITY_CATEGORY=20
  mapped value=Other Significant
  MAJOR=N
  final action=11/19/2001:66 FR 58009

OIRA completed review:
  STAGE=Final Rule
  ECONOMICALLY_SIGNIFICANT=Yes
  DATE_PUBLISHED=2001-11-19

Federal Register final rule:
  Text explicitly says the final regulations meet the criteria for an
  economically significant regulatory action under EO 12866.
```

This means the UA entry is real, but it conflicts with OIRA and the final-rule
text.  For this dataset's purpose, the OIRA/final-text evidence is stronger.

## Why Major Alone Is Excluded

The user-defined category is economically significant rules, not major rules.
Major-rule status and economic-significance status overlap heavily, but they are
not identical.

Therefore the external comparison target uses only:

```text
oira_economically_significant = Yes
OR fr_tracking_econ_significant = 1
OR fr_tracking_3f1_significant = 1
```

The comparison target does not include a rule merely because:

```text
oira_major = Yes
OR fr_tracking_major = 1
```

In the current packaged comparison, major-only records included in the target:

```text
0
```

That count is still retained in an audit file so the exclusion is visible.

## Federal Register Filtering

The pipeline keeps only Federal Register documents that are:

```text
document type: RULE
action: final-like
```

Primary final-like actions include:

- ordinary final rules
- direct final initial rules

The primary universe excludes:

- interim final rules
- temporary final rules
- corrections
- technical amendments
- delay/stay/effective-date support documents
- withdrawals/removals
- direct-final confirmations or support notices
- non-final rule documents

The logic is action-text based because Federal Register metadata has many
variant action strings.  The decision is not that those excluded documents are
unimportant; the decision is that they should not be counted as separate
economically significant final rules.

## CFR Validation

The audited primary file requires local CFR metadata.  This is a practical
guardrail: if a document is truly a rule, it should normally identify CFR parts
or chapters being amended.  The current release also includes provisional and
uncertain rows in audit files rather than silently dropping them.

One parser improvement already included:

```text
If the local parser missed CFR metadata in fr_cfr but fr_subagency contained
phrases like "22 CFR Part 22", the pipeline treats that as valid CFR evidence.
```

## Rule-Level Collapsing

Rows in the rule-level file are rule groups, not RINs and not raw documents.

The grouping logic links documents in the same presidential year when they share
candidate economic-significance RINs.  This is why there can be more unique RINs
than rows:

```text
Rule rows: 1,574
Unique RINs: 1,601
Rows with multiple RINs: 95
```

This is expected.  Some final rules list multiple RINs.

## Validation Status

Against the broad RegStats-style benchmark, the current file is close in shape
but not exact.

```text
Benchmark total, 2000-2024: 1,500
Current CFR-audited total: 1,572
Difference: +72
Mean absolute yearly difference: 8.0
Median absolute yearly difference: 6.0
```

Worst yearly differences in the current release:

```text
2024: +26
2020: -22
2021: -19
2016: +16
2023: +14
2022: +14
```

These differences are not just bugs.  They reflect definition differences,
source disagreements, and the fact that current release construction still uses
external evidence directly.

## Recommended Citation Language

Use language like:

```text
We construct a working universe of economically significant final-rule
candidates by linking parsed Federal Register rule documents, Unified Agenda
RIN-level records, and external OIRA/RegStats economic-significance indicators.
We retain source flags and audit files because economic-significance
classifications sometimes disagree across sources.
```

Avoid language like:

```text
This is the definitive official list of economically significant rules.
```

That would overclaim.

## Recommended Next Rebuild

For a more defensible publication version, the next build should separate:

```text
core_from_ua_priority
external_text_confirmed_additions
external_unconfirmed_audit_queue
major_only_excluded
nonprimary_action_excluded
```

The current package gets us close and gives us the evidence needed to do that
next step cleanly.

