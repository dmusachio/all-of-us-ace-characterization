# All of Us ACE Questionnaire Characterization

This repository contains the analysis code used to characterize the Adverse Childhood Experiences (ACE) questionnaire in the All of Us Research Program. The workflow constructs the eligible and respondent cohorts, derives the 11-item and eight-domain ACE measures, evaluates demographic representativeness and internal consistency, estimates associations with clinical and social outcomes, and creates the manuscript tables and figures.

## Repository layout

```text
notebooks/
  01_analysis_pipeline.ipynb
src/
  config.py
  paths.py
docs/
  output_manifest.md
scripts/
  validate_repository.py
outputs/
  tables/{main,supplementary}/
  figures/{main,supplementary}/
  figure_data/{main,supplementary}/
```

The complete analysis is organized as one top-to-bottom pipeline. This avoids persisting person-level intermediate datasets or duplicating cohort construction across notebooks. Tables and figures are generated when their required aggregate data become available rather than being separated by output type.

## Running the analysis

1. Open the repository within an All of Us Researcher Workbench Controlled Tier workspace containing the required CDR.
2. Review `src/config.py` and confirm the billing project and CDR dataset.
3. Install the Python dependencies listed in `requirements.txt` if they are not already available.
4. Run `notebooks/01_analysis_pipeline.ipynb` from top to bottom.
5. Run `python scripts/validate_repository.py` from the repository root.
6. Review every aggregate output against the applicable All of Us disclosure requirements before committing it.

The billing project and CDR identifiers are intentionally retained in `src/config.py` so the current workspace can run the code. Remove or replace those workspace-specific identifiers before publishing the repository.

## Manuscript output inventory

The pipeline generates:

- Main Tables 1–2
- Supplementary Tables S1–S14, excluding S4 and S7
- Main Figures 1–5
- Supplementary Figures S1–S3

Figure 5 and Supplementary Figure S2 are generated together from the outcome-prevalence-by-ACE-score table. Figure 5 contains the selected strongest dose-response outcomes; Supplementary Figure S2 contains the additional psychiatric, social determinant, and clinical outcomes.

See `docs/output_manifest.md` for the complete numbering map and filenames.

## Data privacy

This repository must not contain person-level All of Us data. Only disclosure-safe aggregate outputs that have passed the applicable All of Us privacy checks should be committed. The `.gitignore` file blocks common person-level and intermediate data formats by default, but it does not replace manual disclosure review.

Notebook outputs and execution counts are cleared in the distributed notebook. Assertions checking cohort structure, counts, score ranges, model rows, and disclosure thresholds have been retained.

## Analysis order

The notebook follows the scientific dependency graph:

1. Eligibility, response completeness, and ACE scoring
2. Main Tables 1–2 and Figures 1–2
3. Demographic burden analyses and Figure 3
4. Clinical and social outcome construction
5. Main Figure 4 and association tables
6. Main Figure 5 and Supplementary Figure S2 generated together
7. Restricted-cohort tables and Supplementary Figure S3

