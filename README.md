# European Energy Data Platform

A production-oriented platform for collecting, transforming, storing, and
serving European energy and weather data.

## Current milestone

Energy API → Python ingestion → PostgreSQL → SQL verification

## Planned components

- Python data ingestion
- MinIO data lake
- dbt transformations
- PostgreSQL data warehouse
- Apache Airflow orchestration
- FastAPI customer API
- Power BI dashboards
- Machine-learning forecasts
- Customer-facing web platform

## Repository structure

- `services/ingestion` — retrieves and validates source data
- `infrastructure` — Docker and local infrastructure
- `docs` — architecture and technical decisions

## Status

Under active development.