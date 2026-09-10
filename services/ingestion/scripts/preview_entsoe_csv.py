from pathlib import Path 
from energy_ingestion.entsoe.csv_loader import read_entsoe_csv

file_path = Path(
    "data/raw/entsoe/hourly_load/monthly_hourly_load_values_2026.csv"
)

rows = read_entsoe_csv(file_path)

for _ in range(5):
    print(next(rows))