# Energy Ingestion Service

Python service responsible for retrieving, validating, and loading European
energy and weather data.

## Responsibilities

- Connect to external data sources
- Preserve original source data
- Validate incoming records
- Normalize timestamps and measurement units
- Load validated records without creating duplicates