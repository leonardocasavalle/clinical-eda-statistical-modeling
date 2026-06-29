Markdown
# Clinical Assay EDA & Statistical Modeling Workflow

## Project Overview
This repository contains an end-to-end Exploratory Data Analysis (EDA) pipeline and parametric hypothesis testing layout designed for clinical trial validation. Utilizing **Python**, **Pandas**, and **SciPy**, the workflow evaluates behavioral kinetics data between two pharmaceutical candidate matrices (Formulation A vs. Formulation B) during active substance absorption screening.

The framework verifies distribution assumptions, establishes baseline descriptive arrays, and provides mathematically sound test conclusions to support data-driven decisions in bio-statistics reporting.

## Statistical Methodologies Implemented
* **Descriptive Frameworks:** Segregated profiling using aggregation tracking metrics (`mean`, `standard deviation`, boundaries).
* **Assumption Validation (Normality Checking):** Employs the **Shapiro-Wilk test** across isolated sample strata to ensure compliance with parametric test constraints ($p > 0.05$).
* **Inferential Testing:** Execution of an **Independent Two-Sample T-Test** to compare target variance populations and identify statistical divergence indicators.

## Tech Stack & Dependencies
* **Language:** Python 3.x
* **Data Handling:** Pandas
* **Scientific Computing:** NumPy, SciPy (Statistical tools suite)
## Execution Layout
To run the evaluation script locally and observe the statistical report metrics, run:
```bash
python eda_modeling.py
Plaintext
=== EXPLORATORY DATA ANALYSIS (EDA) ===

Descriptive Summary Metrics per Group:
               count       mean       std        min        max
group                                                          
Formulation_A     50  25.341142  2.839655  18.318351  30.825219
Formulation_B     50  21.688179  2.830691  15.962002  27.674845

=== HYPOTHESIS TESTING ===
Null Hypothesis (H0): Mean absorption times are equal.
Alternative Hypothesis (H1): Mean absorption times are different.

[Normality Check] Group A Shapiro p-value: 0.7225 | Group B Shapiro p-value: 0.9488

Calculated T-Statistic: 6.4423
Calculated Two-Tailed P-Value: 4.4170e-09

[CONCLUSION]: Reject H0 at alpha=0.05. There is a statistically significant difference in absorpt
