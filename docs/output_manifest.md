# Manuscript output manifest

This manifest defines the final manuscript numbering. Supplementary Tables S4 and S7 are intentionally absent.

## Main tables

| ID | Output filename stem | Description |
|---|---|---|
| Table 1 | `table_1_demographic_comparison_of_ehhwb_eligible_participants_and_ehhwb_respondents` | Demographic comparison of EHHWB-eligible participants and respondents |
| Table 2 | `table_2_distribution_of_8_domain_ace_burden_scores` | Distribution of eight-domain ACE burden scores |

## Supplementary tables

| ID | Output filename stem | Earlier source numbering |
|---|---|---|
| Table S1 | `supplementary_table_s1_valid_ace_response_distribution` | S1 |
| Table S2 | `supplementary_table_s2_ace_item_response_completeness` | S2 |
| Table S3 | `supplementary_table_s3_ace_questionnaire_completion_by_demographic_subgroup` | S3 |
| Table S5 | `supplementary_table_s5_ace_burden_scores_by_demographic_characteristics` | Written as “Supplementary Table 5” |
| Table S6 | `supplementary_table_s6_demographic_predictors_of_elevated_8_domain_ace_burden` | S6 |
| Table S8 | `supplementary_table_s8_internal_consistency_of_8_domain_ace_score` | S8 |
| Table S9 | `supplementary_table_s9_adjusted_associations_between_continuous_8_domain_ace_burden_and_outcomes` | Previously S10 |
| Table S10 | `supplementary_table_s10_unadjusted_associations_between_continuous_8_domain_ace_burden_and_outcomes` | Previously S11 |
| Table S11 | `supplementary_table_s11_prevalence_of_outcomes_by_8_domain_ace_burden_score` | Previously S12 |
| Table S12 | `supplementary_table_s12_continuous_ace_score_associations_with_outcomes` | Previously S13 |
| Table S13 | `supplementary_table_s13_outcome_prevalence_among_participants_with_at_least_2_visits` | Previously S14 |
| Table S14 | `supplementary_table_s14_continuous_8_domain_ace_associations_among_participants_with_at_least_2_visits` | Previously S15 |

## Main figures

| ID | Output | Required input |
|---|---|---|
| Figure 1 | `figure_1a_cohort_flow`; `figure_1b_demographic_representativeness` | Cohort-flow data, Table 1, Tables S1 and S3, and Table 2 |
| Figure 2 | `figure_2a_distribution_of_8_domain_ace_burden_scores`; `figure_2b_empirical_cumulative_distribution_of_8_domain_ace_burden_scores` | Table 2 |
| Figure 3 | `figure_3_demographic_differences_in_8_domain_ace_burden_scores` | Table S5 |
| Figure 4 | `figure_4_associations_between_8_domain_ace_burden_and_outcomes` | Table S9 |
| Figure 5 | `figure_5_dose_response_relationships` | Table S11 |

## Supplementary figures

| ID | Output | Required input |
|---|---|---|
| Figure S1 | `supplementary_figure_s1_birth_year_distribution` | In-memory Table 1 cohort (`table_1_raw`) |
| Figure S2 | `supplementary_figure_s2a_additional_psychiatric_and_social_outcomes`; `supplementary_figure_s2b_additional_clinical_outcomes` | Table S11; generated in the same cell as Figure 5 |
| Figure S3 | `supplementary_figure_s3_main_vs_participants_with_at_least_2_visits_adjusted_associations` | Tables S9 and S14 |

Figure 5 and Supplementary Figure S2 intentionally share one generation cell and one aggregate input table so that outcome groupings, axes, styling, and disclosure checks remain synchronized.
