import pandas as pd

fx = pd.read_csv("data/raw/usd_gel_monthly.csv", parse_dates=["date"])
cpi = pd.read_csv("data/clean/cpi_monthly.csv", parse_dates=["date"])

merged = fx.merge(cpi, on="date", how="inner")
merged.to_csv("data/clean/fx_cpi_monthly.csv", index=False)

print(merged.head())
print(merged.tail())
print(merged.shape)