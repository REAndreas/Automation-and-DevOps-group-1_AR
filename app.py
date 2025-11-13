import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from weather_api_call import get_weather
import matplotlib.ticker as mticker

st.title("Temperatur kommande 24 timmar – Open-Meteo")

cities = {
    "Stockholm": (59.33, 18.07),
    "Oxelösund": (58.67, 17.10),
    "Sankt Petersburg": (59.57, 30.19),
    "Tasjkent": (41.18, 69.16),
    "Malaga": (36.72, 4.42),
    "Reykjavik": (64.14, 21.94)
}

city = st.selectbox("Välj stad", list(cities.keys()))
lat, lon = cities[city]


df = get_weather(lat, lon) 
now = datetime.now()
df_24 = df[(df["time"] >= now) & (df["time"] <= now + timedelta(hours=24))]

df_24 = df_24.copy()  
df_24["time"] = df_24["time"].dt.strftime("%Y-%m-%d %H:%M")

st.subheader(f"Temperaturdata för {city} (kommande 24 timmar)")
st.dataframe(df_24, hide_index=True)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df_24["time"], df_24["temperature"], color="tab:blue", marker="o")
ax.set_title(f"Temperatur kommande 24 timmar – {city}")
ax.set_xlabel("Tid")
ax.set_ylabel("Temperatur (°C)")
ax.grid(True)
ax.yaxis.set_major_locator(mticker.MultipleLocator(0.5))
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
st.pyplot(fig)