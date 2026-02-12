import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# -----------------------------
# CONFIGURATION
# -----------------------------
API_KEY = "2c0ddb72e0478821a0e1017dfdb7a214"
CITY = "Mumbai"
URL = "https://api.openweathermap.org/data/2.5/forecast"

# -----------------------------
# FETCH DATA FROM API
# -----------------------------
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(URL, params=params)
data = response.json()

# -----------------------------
# EXTRACT REQUIRED DATA
# -----------------------------
records = []

for item in data["list"]:
    records.append({
        "datetime": datetime.fromtimestamp(item["dt"]),
        "temperature": item["main"]["temp"],
        "humidity": item["main"]["humidity"],
        "pressure": item["main"]["pressure"]
    })

# Convert to DataFrame
df = pd.DataFrame(records)

# -----------------------------
# VISUALIZATION DASHBOARD
# -----------------------------
plt.figure(figsize=(12, 6))

# Temperature Plot
plt.plot(df["datetime"], df["temperature"], marker='o')
plt.title(f"Temperature Forecast - {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Humidity Plot
plt.figure(figsize=(12, 6))
plt.plot(df["datetime"], df["humidity"], marker='o')
plt.title(f"Humidity Forecast - {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pressure Plot
plt.figure(figsize=(12, 6))
plt.plot(df["datetime"], df["pressure"], marker='o')
plt.title(f"Pressure Forecast - {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Pressure (hPa)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("Dashboard generated successfully!")
