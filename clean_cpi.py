import pandas as pd

raw = pd.read_excel(
    "data/raw/CPI20022026.xlsx",
    header=None,
    skiprows=3,
    nrows=27,
    usecols="B:N",
)
raw.columns = ["year"] + list(range(1, 13))

long = raw.melt(id_vars="year", var_name="month", value_name="cpi")
long["year"] = long["year"].astype(int)
long["cpi"] = pd.to_numeric(long["cpi"], errors="coerce")
long["date"] = pd.to_datetime(dict(year=long["year"], month=long["month"], day=1))

clean = long.dropna(subset=["cpi"]).sort_values("date")[["date", "cpi"]]
clean.to_csv("data/clean/cpi_monthly.csv", index=False)

print(clean.head())
print(clean.tail())
print(clean.shape)