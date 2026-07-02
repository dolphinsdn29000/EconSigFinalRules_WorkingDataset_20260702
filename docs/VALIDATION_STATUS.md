# Validation Status

This note summarizes how the current working dataset validates against external
benchmarks and what the remaining caveats mean.

## Current Release Counts

```text
Rule-level rows: 1,574
CFR-audited rule rows: 1,572
Document candidates: 1,751
```

Current source mix:

```text
UA econ priority + external source: 1,024
UA econ priority only: 430
External source only: 120
```

The external-only rows should be treated as audit-sensitive.  They are useful
because they identify possible UA misses, but they should not be described as
independently constructed from UA+FR alone.

## Broad RegStats-Style Yearly Benchmark

The current CFR-audited rule-level file compared to the broad RegStats-style
benchmark:

```text
Benchmark total, 2000-2024: 1,500
Current CFR-audited total: 1,572
Net difference: +72
Mean absolute yearly difference: 8.0
Median absolute yearly difference: 6.0
```

Largest year-level differences:

| Presidential year | Benchmark | Current CFR-audited | Difference |
|---:|---:|---:|---:|
| 2024 | 124 | 150 | +26 |
| 2020 | 128 | 106 | -22 |
| 2021 | 70 | 51 | -19 |
| 2016 | 99 | 115 | +16 |
| 2023 | 79 | 93 | +14 |
| 2022 | 54 | 68 | +14 |

Interpretation: the shape is plausible, but the file is not benchmark-identical.
This is acceptable for a working dataset, but any paper or public release should
state the source hierarchy and audit status.

## External Econ-Only Comparison

The cleaner validation target excludes major-only rules and includes only
external economic-significance evidence:

```text
oira_economically_significant = Yes
OR fr_tracking_econ_significant = 1
OR fr_tracking_3f1_significant = 1
```

Result:

```text
External econ-only target docs: 1,157
Found by UA-priority construction: 1,039
Missing from UA-priority construction: 118
Major-only records included: 0
```

Missing reasons:

| Reason | Count |
|---|---:|
| RIN in UA, but UA priority is not econ | 95 |
| RIN has UA econ somewhere, but doc not reached by construction path | 14 |
| RIN not found in UA | 5 |
| External econ doc has no RIN in target record | 4 |

## What This Means

The main validation lesson is:

```text
UA priority alone misses real economically significant final rules.
```

The clearest audited example is `0960-AB01`, where:

- UA says `Other Significant`.
- OIRA final-rule review says `ECONOMICALLY_SIGNIFICANT=Yes`.
- The final Federal Register text explicitly says the final regulations meet
  the criteria for an economically significant regulatory action under EO 12866.

This is why the current package keeps external evidence and conflict audit files
instead of pretending one source is perfect.

## What Is Good Enough For Now

The current release is good enough for:

- exploratory empirical work,
- linked FR/UA inspection,
- identifying candidate economically significant final rules,
- auditing source conflicts,
- creating proposal/final linkage extensions.

It is not yet ideal for:

- claiming an official definitive universe,
- publication without source hierarchy notes,
- treating every external-only row as automatically correct.

