from pathlib import Path
from energy_ingestion.entsoe.postgres_loader import load_entsoe_hourly_load

file_path = Path(
    "data/raw/entsoe/hourly_load/monthly_hourly_load_values_2026.csv"
)

load_entsoe_hourly_load(file_path)

print("ENTSO-E hourly load ingestion completed.")