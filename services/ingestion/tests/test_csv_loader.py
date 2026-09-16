import pytest

from energy_ingestion.entsoe.csv_loader import read_entsoe_csv

def test_read_entsoe_csv(tmp_path):
    csv_file = tmp_path/"entose.csv"

    csv_file.write_text(
        "MeasureItem\tDateUTC\tDateShort\tTimeFrom\tTimeTo\t"
        "CountryCode\tCov_ratio\tValue\tValue_ScaleTo100\t"
        "CreateDate\tUpdateDate\n"
        "Monthly Hourly Load Values\t01-01-2026 00:00\t"
        "01-01-2026\t00:00\t01:00\tBE\t100\t8408.2725000\t"
        "8408.2725000\t01-09-2026 09:06:17\t28-04-2026 10:40:03\n",
        encoding="utf-8",
    )

    rows=read_entsoe_csv(csv_file)

    row=next(rows)

    assert row["CountryCode"] == "BE"
    assert row["Value"] == "8408.2725000"

def test_read_entsoe_csv_rejects_wrong_schema(tmp_path):
    csv_file = tmp_path / "bad_entsoe.csv"

    csv_file.write_text(
        "CountryCode\tValue\n"
        "BE\t8408\n",
        encoding="utf-8",
    )

    rows = read_entsoe_csv(csv_file)

    with pytest.raises(ValueError):
        next(rows)