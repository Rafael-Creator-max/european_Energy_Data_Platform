from itertools import islice
from pathlib import Path

from energy_ingestion.database.connection import get_connection
from energy_ingestion.entsoe.csv_loader import read_entsoe_csv

INSERT_SQL = """
    INSERT INTO raw.entsoe_hourly_load(
        measure_item,
        date_utc,
        date_short,
        time_from,
        time_to,
        country_code,
        cov_ratio,
        value,
        value_scale_to_100,
        create_date,
        update_date
    )

    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

def load_entsoe_hourly_load(file_path:Path,limit: int | None=None) -> None:
    rows = read_entsoe_csv(file_path)

    if limit is not None:
        rows = islice(rows,limit)

    records = (
        (
        row["MeasureItem"],
        row["DateUTC"],
        row["DateShort"],
        row["TimeFrom"],
        row["TimeTo"],
        row["CountryCode"],
        row["Cov_ratio"],
        row["Value"],
        row["Value_ScaleTo100"],
        row["CreateDate"],
        row["UpdateDate"],
        )
        for row in rows
    )

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.executemany(INSERT_SQL,records)