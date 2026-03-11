import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Bike Sharing Data Dashboard")

# =========================
# Load Data
# =========================

day_df = pd.read_csv("dashboard/main_data.csv")
hour_df = pd.read_csv("data/hour.csv")

# =========================
# Label Mapping
# =========================

season_map = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}

weather_map = {
    1: "Clear",
    2: "Mist",
    3: "Light Rain/Snow",
    4: "Heavy Rain/Snow"
}

day_df["season"] = day_df["season"].map(season_map)
day_df["weathersit"] = day_df["weathersit"].map(weather_map)

# =========================
# Filter Season
# =========================

season_option = st.selectbox(
    "Select Season",
    day_df["season"].unique()
)

filtered_df = day_df[day_df["season"] == season_option]

# =========================
# 1. Weather vs Bike Rental
# =========================

st.subheader("Average Bike Rentals by Weather Condition")

weather_data = (
    filtered_df.groupby("weathersit")["cnt"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots()

sns.barplot(
    data=weather_data,
    x="weathersit",
    y="cnt",
    palette="viridis",
    ax=ax
)

ax.set_xlabel("Weather Condition")
ax.set_ylabel("Average Bike Rentals")

st.pyplot(fig)

# =========================
# 2. Peak Hour Rental
# =========================

st.subheader("Average Bike Rentals by Hour (Working Day vs Holiday)")

hour_data = (
    hour_df.groupby(["workingday","hr"])["cnt"]
    .mean()
    .reset_index()
)

# Label workingday agar jelas
hour_data["workingday"] = hour_data["workingday"].map({
    0: "Holiday / Weekend",
    1: "Working Day"
})

hour_data = hour_data.sort_values("hr")

fig, ax = plt.subplots(figsize=(10,5))

sns.lineplot(
    data=hour_data,
    x="hr",
    y="cnt",
    hue="workingday",
    marker="o",
    ax=ax
)

ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Average Bike Rentals")
ax.set_xticks(range(0,24))
ax.legend(title="Day Type")

st.pyplot(fig)

# =========================
# 3. Casual vs Registered
# =========================

st.subheader("Total Rentals by User Type")

user_data = (
    day_df[["casual","registered"]]
    .sum()
    .reset_index()
)

user_data.columns = ["User Type","Total Rentals"]

fig, ax = plt.subplots()

sns.barplot(
    data=user_data,
    x="User Type",
    y="Total Rentals",
    palette="Set2",
    ax=ax
)

ax.set_xlabel("User Type")
ax.set_ylabel("Total Rentals")

st.pyplot(fig)