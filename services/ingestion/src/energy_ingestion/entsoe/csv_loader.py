import csv
from collections.abc import Iterator
from pathlib import Path

EXPECTED_COLUMNS = [
    "MeasureItem",
    "DateUTC",
    "DateShort",
    "TimeFrom",
    "TimeTo",
    "CountryCode",
    "Cov_ratio",
    "Value",
    "Value_ScaleTo100",
    "CreateDate",
    "UpdateDate",

]

def read_entsoe_csv(file_path: Path) -> Iterator[dict[str,str]]:
    """Read ENTSO-E hourly load data one row at a time."""
    with file_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline="",
    ) as csv_file :

        reader=csv.DictReader(
            csv_file,
            delimiter="\t"
        )

        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(
                  "Unexpected ENTSO-E CSV schema.\n"
                f"Expected: {EXPECTED_COLUMNS}\n"
                f"Received: {reader.fieldnames}"
            )
        yield from reader