import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean/fx_cpi_monthly.csv", parse_dates=["date"])

df["usd_index"] = df["usd_gel"] / df["usd_gel"].iloc[0] * 100
df["cpi_index"] = df["cpi"] / df["cpi"].iloc[0] * 100

print("USD/GEL change since Jan 2015:", round(df["usd_index"].iloc[-1] - 100, 1), "%")
print("Consumer prices change since Jan 2015:", round(df["cpi_index"].iloc[-1] - 100, 1), "%")

plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["usd_index"], label="USD/GEL")
plt.plot(df["date"], df["cpi_index"], label="CPI (prices)")
plt.title("USD/GEL vs consumer prices (Jan 2015 = 100)")
plt.xlabel("Year")
plt.ylabel("Index (Jan 2015 = 100)")
plt.legend()
plt.grid(True)
plt.savefig("dashboard/fx_vs_cpi.png")
plt.show()