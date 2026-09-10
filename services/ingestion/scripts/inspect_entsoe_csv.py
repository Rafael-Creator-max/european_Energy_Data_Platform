import pandas as pd

df=pd.read_csv(
    "data/raw/entsoe/hourly_load/monthly_hourly_load_values_2026.csv",
    sep="\t",
    encoding="utf-8-sig"
)

print(df.shape)

print(df.columns) 

print(df.head())

print(df.dtypes)

print(df.isna().sum())

print(df["CountryCode"].unique())

print(df["CountryCode"].nunique())

dates = pd.to_datetime(df["DateUTC"],format="%d-%m-%Y %H:%M")
print(dates.min())

print(dates.max())

print(df.duplicated(
    subset=["MeasureItem","DateUTC","CountryCode"]
).sum())

print(df.columns.tolist())