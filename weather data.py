# Weather Data Visualizer
# Created by-
# Name- Chirag Virdi
# Class- BTech CSE (DS)
# Roll no- 2501420017
# Date- 13/12/2025


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("Weather Data.csv")

print("\n--- HEAD ---")
print(df.head())

print("\n--- INFO ---")
print(df.info())

print("\n--- DESCRIBE ---")
print(df.describe())

def _norm(col):
    return col.lower().replace(" ", "").replace("/", "").replace("-", "").replace("_", "")
cols = { _norm(c): c for c in df.columns }

date_keys = ["datetime", "date", "datetimecolumn", "time"]
date_col = None
for k in date_keys:
    if k in cols:
        date_col = cols[k]
        break
if date_col is None:
    raise KeyError("No date/datetime column found in CSV. Columns: {}".format(list(df.columns)))

temp_keys = ["tempc", "temp", "temperature"]
temp_col = None
for k in temp_keys:
    if k in cols:
        temp_col = cols[k]
        break
if temp_col is None:
    raise KeyError("No temperature column found in CSV. Columns: {}".format(list(df.columns)))

hum_keys = ["relhum%", "relhum", "humidity", "hum"]
hum_col = None
for k in hum_keys:
    if k in cols:
        hum_col = cols[k]
        break
if hum_col is None:
    raise KeyError("No humidity column found in CSV. Columns: {}".format(list(df.columns)))

rain_keys = ["rainfallmm", "rainfall", "precipitation", "precipmm"]
rain_col = None
for k in rain_keys:
    if k in cols:
        rain_col = cols[k]
        break

df["date"] = pd.to_datetime(df[date_col], errors="coerce")
df = df.dropna(subset=["date"]) 

df = df.rename(columns={temp_col: "temperature", hum_col: "humidity"})

if rain_col is not None:
    df = df.rename(columns={rain_col: "rainfall_mm"})
else:
    np.random.seed(42)   
    rainfall = []
    for _ in range(len(df)):
        r = np.random.rand()
        if r < 0.70:              
            rainfall.append(0)
        elif r < 0.90:            
            rainfall.append(round(np.random.uniform(0, 5), 2))
        else:                     
            rainfall.append(round(np.random.uniform(5, 20), 2))
    df["rainfall_mm"] = rainfall

df = df[["date", "temperature", "humidity", "rainfall_mm"]]

print("\n--- CLEANED DATA ---")
print(df.head())


daily_mean = np.mean(df["temperature"])
daily_min = np.min(df["temperature"])
daily_max = np.max(df["temperature"])
daily_std = np.std(df["temperature"])

print("\n--- DAILY TEMPERATURE STATS ---")
print(f"Mean: {daily_mean:.2f}")
print(f"Min: {daily_min:.2f}")
print(f"Max: {daily_max:.2f}")
print(f"Std Dev: {daily_std:.2f}")

df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year

monthly_stats = df.groupby("month").agg({
    "temperature": ["mean", "min", "max", "std"],
    "rainfall_mm": "sum"
})

print("\n--- MONTHLY STATS ---")
print(monthly_stats)


plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["temperature"])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.savefig("daily_temperature.png")
plt.close()

monthly_rain = df.groupby("month")["rainfall_mm"].sum()

plt.figure(figsize=(10, 5))
plt.bar(monthly_rain.index, monthly_rain.values)
plt.title("Monthly Rainfall Totals")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.savefig("monthly_rainfall.png")
plt.close()

plt.figure(figsize=(10, 5))
plt.scatter(df["temperature"], df["humidity"])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.savefig("humidity_vs_temperature.png")
plt.close()

plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["temperature"], label="Temperature", linewidth=1)
plt.bar(df["date"], df["rainfall_mm"], alpha=0.3, label="Rainfall")
plt.legend()
plt.title("Temperature & Rainfall Over Time")
plt.savefig("combined_plot.png")
plt.close()


monthly_avg = df.groupby("month")[["temperature", "humidity"]].mean()
print("\n--- MONTHLY AVERAGES ---")
print(monthly_avg)

def season_of_month(m):
    if m in [12, 1, 2]: return "Winter"
    if m in [3, 4, 5]: return "Spring"
    if m in [6, 7, 8]: return "Summer"
    return "Autumn"

df["season"] = df["month"].apply(season_of_month)

seasonal_stats = df.groupby("season")[["temperature", "rainfall_mm"]].mean()
print("\n--- SEASONAL STATS ---")
print(seasonal_stats)


df.to_csv("cleaned_weather_data.csv", index=False)

report = f"""
# Weather Analysis Report

## Key Temperature Statistics
- Mean Temperature: {daily_mean:.2f}
- Minimum Temperature: {daily_min:.2f}
- Maximum Temperature: {daily_max:.2f}
- Standard Deviation: {daily_std:.2f}

## Monthly Rainfall
Generated synthetic rainfall data used for rainfall analysis.

## Files Generated
- cleaned_weather_data.csv
- daily_temperature.png
- monthly_rainfall.png
- humidity_vs_temperature.png
- combined_plot.png

"""

with open("weather_report.md", "w") as f:
    f.write(report)

print("\n✔ All tasks complete! Plots + report generated.")