Python
import numpy as np
import pandas as pd
from scipy import stats


def generate_clinical_trial_data():
    """Simulates clinical assay variables for two formulations of Lidocaine HCl

    (Formulation A: Standard vs. Formulation B: Optimized Matrix).
    """
    np.random.seed(42)
    n_samples = 50

    # Simulate absorption time in minutes (Formulation B is designed to be faster)
    formulation_a = np.random.normal(loc=25.5, scale=3.2, size=n_samples)
    formulation_b = np.random.normal(loc=21.8, scale=2.9, size=n_samples)

    data = pd.DataFrame(
        {
            "patient_id": [f"PID_{i:03d}" for i in range(1, 2 * n_samples + 1)],
            "group": ["Formulation_A"] * n_samples + ["Formulation_B"] * n_samples,
            "absorption_time_mins": np.concatenate(
                [formulation_a, formulation_b]
            ),
        }
    )
    return data


def perform_statistical_analysis(df):
    """Executes descriptive statistics and an independent sample t-test."""
    print("=== EXPLORATORY DATA ANALYSIS (EDA) ===")

    # 1. Descriptive Statistics by Group
    grouped_stats = df.groupby("group")["absorption_time_mins"].agg(
        ["count", "mean", "std", "min", "max"]
    )
    print("\nDescriptive Summary Metrics per Group:")
    print(grouped_stats)

    print("\n=== HYPOTHESIS TESTING ===")
    print("Null Hypothesis (H0): Mean absorption times are equal.")
    print("Alternative Hypothesis (H1): Mean absorption times are different.")

    # Extract groups for parametric testing
    group_a = df[df["group"] == "Formulation_A"]["absorption_time_mins"]
    group_b = df[df["group"] == "Formulation_B"]["absorption_time_mins"]

    # 2. Shapiro-Wilk Test for Normality Assumptions
    _, p_norm_a = stats.shapiro(group_a)
    _, p_norm_b = stats.shapiro(group_b)
    print(
        f"\n[Normality Check] Group A Shapiro p-value: {p_norm_a:.4f} | Group B Shapiro p-value: {p_norm_b:.4f}"
    )

    # 3. Two-Sample Independent T-Test (Parametric analysis)
    t_stat, p_val = stats.ttest_ind(group_a, group_b, equal_var=True)
    print(f"\nCalculated T-Statistic: {t_stat:.4f}")
    print(f"Calculated Two-Tailed P-Value: {p_val:.4e}")

    # 4. Statistical Conclusion
    alpha = 0.05
    if p_val < alpha:
        print(
            f"\n[CONCLUSION]: Reject H0 at alpha={alpha}. There is a statistically significant "
            "difference in absorption efficiency between the two formulations."
        )
    else:
        print(
            f"\n[CONCLUSION]: Fail to reject H0. No statistically significant evidence "
            "of variation between formulations."
        )


if __name__ == "__main__":
    # Execute analytical workflow
    assay_data = generate_clinical_trial_data()
    perform_statistical_analysis(assay_data)
