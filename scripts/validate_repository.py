"""Validate repository structure and manuscript numbering without running analyses."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_NOTEBOOK = ROOT / "notebooks" / "01_analysis_pipeline.ipynb"

EXPECTED_SUPPLEMENTARY_TABLE_IDS = (
    "s1",
    "s2",
    "s3",
    "s5",
    "s6",
    "s8",
    "s9",
    "s10",
    "s11",
    "s12",
    "s13",
    "s14",
)

EXPECTED_MAIN_FIGURES = tuple(f"figure_{number}" for number in range(1, 6))
EXPECTED_SUPPLEMENTARY_FIGURES = tuple(
    f"supplementary_figure_s{number}" for number in range(1, 4)
)


def notebook_source(notebook: dict) -> str:
    return "\n".join(
        "".join(cell.get("source", [])) for cell in notebook.get("cells", [])
    )


def main() -> int:
    errors: list[str] = []

    if not ANALYSIS_NOTEBOOK.exists():
        print(f"Missing notebook: {ANALYSIS_NOTEBOOK.relative_to(ROOT)}")
        return 1

    notebook = json.loads(ANALYSIS_NOTEBOOK.read_text(encoding="utf-8"))

    for index, cell in enumerate(notebook.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        if cell.get("outputs"):
            errors.append(f"Cell {index} contains outputs")
        if cell.get("execution_count") is not None:
            errors.append(f"Cell {index} has an execution count")

    figure_markdown_cells = [
        (index, "".join(cell.get("source", [])))
        for index, cell in enumerate(notebook.get("cells", []))
        if cell.get("cell_type") == "markdown"
        and "## " in "".join(cell.get("source", []))
        and "Figure" in "".join(cell.get("source", []))
    ]
    for index, markdown_source in figure_markdown_cells:
        if "**Required input" not in markdown_source and (
            "**Required upstream section" not in markdown_source
        ):
            errors.append(f"Figure heading in cell {index} lacks dependency instructions")

    source = notebook_source(notebook).lower()

    missing_tables = [
        table_id
        for table_id in EXPECTED_SUPPLEMENTARY_TABLE_IDS
        if f"supplementary_table_{table_id}" not in source
    ]
    missing_main_figures = [
        figure_id for figure_id in EXPECTED_MAIN_FIGURES if figure_id not in source
    ]
    missing_supplementary_figures = [
        figure_id
        for figure_id in EXPECTED_SUPPLEMENTARY_FIGURES
        if figure_id not in source
    ]

    if missing_tables:
        errors.append("Missing supplementary table IDs: " + ", ".join(missing_tables))
    if missing_main_figures:
        errors.append("Missing main figure IDs: " + ", ".join(missing_main_figures))
    if missing_supplementary_figures:
        errors.append(
            "Missing supplementary figure IDs: "
            + ", ".join(missing_supplementary_figures)
        )

    dose_response_cells = [
        "".join(cell.get("source", [])).lower()
        for cell in notebook.get("cells", [])
        if cell.get("cell_type") == "code"
    ]
    if not any(
        "figure_5_dose_response_relationships" in cell
        and "supplementary_figure_s2" in cell
        for cell in dose_response_cells
    ):
        errors.append(
            "Figure 5 and Supplementary Figure S2 are not generated in one code cell"
        )

    forbidden_labels = (
        "supplementary_table_s15",
        "supplementary_figure_s3_birth_year",
        "figure_5a_strongest",
        "figure_5b_additional",
        "figure_5c_additional",
    )
    present_forbidden = [label for label in forbidden_labels if label in source]
    if present_forbidden:
        errors.append("Obsolete numbering remains: " + ", ".join(present_forbidden))

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository structure and manuscript numbering are valid.")
    print("Figure 5 and Supplementary Figure S2 share one generation cell.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
