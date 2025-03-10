import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset day.csv dan hour.csv
day_df = pd.read_csv("https://raw.githubusercontent.com/dewiyulianaa/Analyze-Bike-Sharing-dataset-using-streamlit-dashboard/main/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/dewiyulianaa/Analyze-Bike-Sharing-dataset-using-streamlit-dashboard/main/hour.csv")

# Manual Grouping berdasarkan jumlah penyewaan sepeda
cnt_describe = day_df['cnt'].describe()
q1, q3 = cnt_describe['25%'], cnt_describe['75%']

def categorize_usage(cnt):
    if cnt < q1:
        return 'Low Usage'
    elif cnt > q3:
        return 'High Usage'
    else:
        return 'Medium Usage'

day_df["usage_category"] = day_df["cnt"].apply(categorize_usage)

# Konversi dteday ke datetime
day_df["dteday"] = pd.to_datetime(day_df["dteday"])

# Sidebar - Filter Rentang Waktu
st.sidebar.header("Filter Data")
start_date = pd.to_datetime(st.sidebar.date_input("Start Date", day_df["dteday"].min()))
end_date = pd.to_datetime(st.sidebar.date_input("End Date", day_df["dteday"].max()))

# Filter data berdasarkan rentang waktu
filtered_day_df = day_df[(day_df["dteday"] >= start_date) & (day_df["dteday"] <= end_date)]
filtered_hour_df = hour_df[hour_df["dteday"].isin(filtered_day_df["dteday"].astype(str))]

# Header Dashboard
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Analisis data penyewaan sepeda berdasarkan musim, jam penyewaan.")

### Penyewaan Berdasarkan Musim
st.subheader("🌤 Penyewaan Sepeda Berdasarkan Musim")
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
filtered_day_df["season"] = filtered_day_df["season"].map(season_mapping)

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x="season", y="cnt", data=filtered_day_df, estimator=sum, palette="coolwarm", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Penyewaan")
ax.set_title("Total Penyewaan Berdasarkan Musim")
st.pyplot(fig)

### Pola Penyewaan Berdasarkan Jam
st.subheader("⏰ Penyewaan Sepeda Berdasarkan Jam dalam Sehari")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x="hr", y="cnt", ci= None, marker='o', data=filtered_hour_df, palette="Blues")
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title("Rata-rata Penyewaan Sepeda per Jam dalam Sehari")
st.pyplot(fig)

### Pola Penyewaan Berdasarkan Kategori
st.subheader("📈 Tren Penyewaan Sepeda Berdasarkan Kategori")
fig, ax = plt.subplots(figsize=(10,5))
sns.countplot(x="usage_category", data=filtered_day_df, palette="coolwarm")
ax.set_xlabel("Kategori Penggunaan")
ax.set_ylabel("Jumlah Hari")
ax.set_title("Trend Penggunaan Sepeda (Low, Medium, High Usage)")
st.pyplot(fig)

### Pengaruh Cuaca terhadap Penggunaan Sepeda
st.subheader("🌦 Pengaruh Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x='weathersit', y='cnt', hue='usage_category', data=filtered_day_df, palette='coolwarm')
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_title("Pengaruh Cuaca terhadap Penggunaan Sepeda")
st.pyplot(fig)

# Footer
st.caption("Data dari dataset Bike Sharing. Dashboard dibuat oleh Dewi Yuliana 🚀")
