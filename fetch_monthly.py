import time
import requests
import pandas as pd

url = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/"
dates = pd.date_range("2015-01-01", "2026-11-01", freq="MS")

rows = []
for d in dates:
    date_str = d.strftime("%Y-%m-%d")
    try:
        response = requests.get(url, params={"date": date_str}, timeout=30)
        data = response.json()
        for currency in data[0]["currencies"]:
            if currency["code"] == "USD":
                rows.append({"date": date_str, "usd_gel": currency["rate"]})
        print(date_str, "OK")
    except Exception as e:
        print(date_str, "ERROR", e)
    time.sleep(0.5)

df = pd.DataFrame(rows)
df.to_csv("data/raw/usd_gel_monthly.csv", index=False)
print(df.shape)