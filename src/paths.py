"""Repository-relative input and output paths."""

from pathlib import Path


def find_repository_root(start: Path | None = None) -> Path:
    """Return the nearest parent containing this repository's marker files."""
    current = (start or Path.cwd()).resolve()

    for candidate in (current, *current.parents):
        if (candidate / "src" / "config.py").exists() and (
            candidate / "notebooks"
        ).exists():
            return candidate

    raise FileNotFoundError(
        "Could not locate the repository root. Run the notebook from within "
        "the cloned aou-ace-characterization repository."
    )


REPO_ROOT = find_repository_root()
OUTPUT_ROOT = REPO_ROOT / "outputs"

TABLES_MAIN_DIR = OUTPUT_ROOT / "tables" / "main"
TABLES_SUPPLEMENTARY_DIR = OUTPUT_ROOT / "tables" / "supplementary"

FIGURES_MAIN_DIR = OUTPUT_ROOT / "figures" / "main"
FIGURES_SUPPLEMENTARY_DIR = OUTPUT_ROOT / "figures" / "supplementary"

FIGURE_DATA_MAIN_DIR = OUTPUT_ROOT / "figure_data" / "main"
FIGURE_DATA_SUPPLEMENTARY_DIR = OUTPUT_ROOT / "figure_data" / "supplementary"


def ensure_output_directories() -> None:
    """Create every expected output directory if it does not exist."""
    for directory in (
        TABLES_MAIN_DIR,
        TABLES_SUPPLEMENTARY_DIR,
        FIGURES_MAIN_DIR,
        FIGURES_SUPPLEMENTARY_DIR,
        FIGURE_DATA_MAIN_DIR,
        FIGURE_DATA_SUPPLEMENTARY_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)
