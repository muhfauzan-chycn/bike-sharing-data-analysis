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

day_df["season"] = day_df["season"].replace(season_map)
day_df["weathersit"] = day_df["weathersit"].replace(weather_map)

# =========================
# Filter Season
# =========================

season_option = st.selectbox(
    "Select Season",
    sorted(day_df["season"].dropna().unique())
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

if not weather_data.empty:

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

else:
    st.write("No data available for this season.")


# =========================
# 2. Peak Hour Rental
# =========================

st.subheader("Average Bike Rentals by Hour")

# membuat salinan dataframe agar tidak mengubah data asli
hour_plot_df = hour_df.copy()

# ubah label workingday agar lebih jelas
hour_plot_df["workingday"] = hour_plot_df["workingday"].map({
    0: "Holiday / Weekend",
    1: "Working Day"
})

fig, ax = plt.subplots(figsize=(10,5))

sns.lineplot(
    data=hour_plot_df,
    x="hr",
    y="cnt",
    hue="workingday",
    ax=ax
)

ax.set_title("Average Bike Rentals by Hour")
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