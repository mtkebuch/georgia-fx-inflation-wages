import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/usd_gel_monthly.csv", parse_dates=["date"])

plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["usd_gel"])
plt.title("USD/GEL exchange rate (first day of each month)")
plt.xlabel("Year")
plt.ylabel("GEL per 1 USD")
plt.grid(True)
plt.savefig("dashboard/usd_gel.png")
plt.show()