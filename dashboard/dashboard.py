import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Bike Sharing Data Dashboard")

#load data
df = pd.read_csv("dashboard/main_data.csv")

season_option = st.selectbox(
    "Select Season",
    df["season"].unique()
)


filtered_df = df[df["season"] == season_option]

# Weather vs Bike Rental
st.subheader("Average Bike Rentals by Weather")

weather_data = filtered_df.groupby("weathersit")["cnt"].mean()

fig, ax = plt.subplots()
sns.barplot(x=weather_data.index, y=weather_data.values, ax=ax)

ax.set_xlabel("Weather Condition")
ax.set_ylabel("Average Rentals")

st.pyplot(fig)

# Season vs Bike Rental
st.subheader("Average Bike Rentals by Season")

season_data = df.groupby("season")["cnt"].mean()

fig, ax = plt.subplots()
sns.barplot(x=weather_data.index, y=weather_data.values, ax=ax)

ax.set_xlabel("Season")
ax.set_ylabel("Average Rentals")

st.pyplot(fig)

# Casual vs Registered
st.subheader("Average Bike Rentals by Type")

user_data = df.groupby("casual")["registered"].mean()

fig, ax = plt.subplots()
sns.barplot(x=weather_data.index, y=weather_data.values, ax=ax)

ax.set_xlabel("User Type")
ax.set_ylabel("Average Rentals")

st.pyplot(fig)