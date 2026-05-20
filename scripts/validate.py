#!/usr/bin/env python3
"""
Bankable Compute Index — schema validator

Validates that data/regions.csv conforms to:
  - the indicator IDs defined in schema/scorecard.yaml
  - the source IDs defined in data/sources.yaml
  - the allowed confidence states: observed, estimated, missing

Exits with status 1 if any validation errors are found.

License: MIT
"""

import csv
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schema" / "scorecard.yaml"
SOURCES_PATH = REPO_ROOT / "data" / "sources.yaml"
REGIONS_PATH = REPO_ROOT / "data" / "regions.csv"

VALID_CONFIDENCE = {"observed", "estimated", "missing"}
EXPECTED_COLUMNS = {
    "region",
    "indicator_id",
    "score",
    "confidence",
    "as_of_date",
    "source_id",
    "notes",
}


def load_yaml(path: Path):
    with path.open() as f:
        return yaml.safe_load(f)


def main() -> int:
    errors = []

    # Load schema and sources
    if not SCHEMA_PATH.exists():
        print(f"ERROR: schema not found at {SCHEMA_PATH}")
        return 2
    if not SOURCES_PATH.exists():
        print(f"ERROR: sources not found at {SOURCES_PATH}")
        return 2
    if not REGIONS_PATH.exists():
        print(f"ERROR: regions.csv not found at {REGIONS_PATH}")
        return 2

    schema = load_yaml(SCHEMA_PATH)
    sources = load_yaml(SOURCES_PATH)

    valid_indicator_ids = {ind["id"] for ind in schema.get("indicator_schema", [])}
    valid_source_ids = {s["id"] for s in sources.get("sources", [])}

    # Validate regions.csv
    with REGIONS_PATH.open() as f:
        reader = csv.DictReader(f)

        # Column-set check
        actual_columns = set(reader.fieldnames or [])
        if actual_columns != EXPECTED_COLUMNS:
            missing = EXPECTED_COLUMNS - actual_columns
            extra = actual_columns - EXPECTED_COLUMNS
            if missing:
                errors.append(f"regions.csv: missing columns: {sorted(missing)}")
            if extra:
                errors.append(f"regions.csv: unexpected columns: {sorted(extra)}")

        for row_num, row in enumerate(reader, start=2):
            indicator_id = (row.get("indicator_id") or "").strip()
            confidence = (row.get("confidence") or "").strip()
            source_id = (row.get("source_id") or "").strip()
            score = (row.get("score") or "").strip()

            # indicator_id must be known
            if indicator_id and indicator_id not in valid_indicator_ids:
                errors.append(
                    f"regions.csv row {row_num}: unknown indicator_id "
                    f"'{indicator_id}' (valid: {sorted(valid_indicator_ids)})"
                )

            # confidence must be in the allowed set
            if confidence not in VALID_CONFIDENCE:
                errors.append(
                    f"regions.csv row {row_num}: invalid confidence "
                    f"'{confidence}' (valid: {sorted(VALID_CONFIDENCE)})"
                )

            # source_id, when present, must be in the source ledger
            if source_id and source_id not in valid_source_ids:
                errors.append(
                    f"regions.csv row {row_num}: unknown source_id "
                    f"'{source_id}' (not in data/sources.yaml)"
                )

            # If confidence is 'missing', score should be empty.
            # If confidence is 'observed' or 'estimated', score should be 0-5.
            if confidence in {"observed", "estimated"}:
                if not score:
                    errors.append(
                        f"regions.csv row {row_num}: confidence is "
                        f"'{confidence}' but score is empty"
                    )
                else:
                    try:
                        s = int(score)
                        if s < 0 or s > 5:
                            errors.append(
                                f"regions.csv row {row_num}: score {s} "
                                f"outside 0-5 range"
                            )
                    except ValueError:
                        errors.append(
                            f"regions.csv row {row_num}: score "
                            f"'{score}' is not an integer"
                        )

    if errors:
        print("Validation FAILED with the following errors:\n")
        for e in errors:
            print(f"  - {e}")
        print(f"\nTotal errors: {len(errors)}")
        return 1

    print("All validations passed.")
    print(
        f"  Schema indicators: {len(valid_indicator_ids)}, "
        f"sources: {len(valid_source_ids)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
