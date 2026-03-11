import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Bike Sharing Data Dashboard")

# Load data
df = pd.read_csv("dashboard/main_data.csv")


# Filter Season

season_option = st.selectbox(
    "Select Season",
    df["season"].unique()
)

filtered_df = df[df["season"] == season_option]


# 1. Weather vs Bike Rental

st.subheader("Average Bike Rentals by Weather Condition")

weather_data = filtered_df.groupby("weathersit")["cnt"].mean().reset_index()

fig, ax = plt.subplots()

sns.barplot(
    data=weather_data,
    x="weathersit",
    y="cnt",
    ax=ax
)

ax.set_xlabel("Weather Condition")
ax.set_ylabel("Average Bike Rentals")

st.pyplot(fig)


# 2. Peak Hour Rental

st.subheader("Average Bike Rentals by Hour")

hour_data = df.groupby("hr")["cnt"].mean().reset_index()

fig, ax = plt.subplots()

sns.lineplot(
    data=hour_data,
    x="hr",
    y="cnt",
    marker="o",
    ax=ax
)

ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Average Bike Rentals")

st.pyplot(fig)


# 3. Casual vs Registered

st.subheader("Total Rentals by User Type")

user_data = df[["casual","registered"]].sum()

fig, ax = plt.subplots()

sns.barplot(
    x=user_data.index,
    y=user_data.values,
    ax=ax
)

ax.set_xlabel("User Type")
ax.set_ylabel("Total Rentals")

st.pyplot(fig)