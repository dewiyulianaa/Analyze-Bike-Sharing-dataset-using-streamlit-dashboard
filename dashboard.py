import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset yang sudah digabung
df = pd.read_csv("merged_bike_data.csv")


# Manual Grouping berdasarkan jumlah penyewaan sepeda
cnt_describe = df['cnt_day'].describe()
q1, q3 = cnt_describe['25%'], cnt_describe['75%']

def categorize_usage(cnt):
    if cnt < q1:
        return 'Low Usage'
    elif cnt > q3:
        return 'High Usage'
    else:
        return 'Medium Usage'

df["usage_category"] = df["cnt_day"].apply(categorize_usage)

# Konversi dteday ke datetime
df["dteday"] = pd.to_datetime(df["dteday"])

# Sidebar - Filter Rentang Waktu
st.sidebar.header("Filter Data")
start_date = pd.to_datetime(st.sidebar.date_input("Start Date", df["dteday"].min()))
end_date = pd.to_datetime(st.sidebar.date_input("End Date", df["dteday"].max()))

# Filter data berdasarkan rentang waktu
filtered_df = df[(df["dteday"] >= start_date) & (df["dteday"] <= end_date)]

# Header Dashboard
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Analisis data penyewaan sepeda berdasarkan musim, jam penyewaan.")

###  Penyewaan Berdasarkan Musim**
st.subheader("🌤 Penyewaan Sepeda Berdasarkan Musim")
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
filtered_df["season_day"] = filtered_df["season_day"].map(season_mapping)

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x="season_day", y="cnt_day", data=filtered_df, estimator=sum, palette="coolwarm", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Penyewaan")
ax.set_title("Total Penyewaan Berdasarkan Musim")
st.pyplot(fig)

### Pola Penyewaan Berdasarkan Jam**
st.subheader("⏰ Penyewaan Sepeda Berdasarkan Jam dalam sehari")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x="hr", y="cnt_hour", data=filtered_df, palette="Blues")
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title("Rata-rata Penyewaan Sepeda per Jam dalam Sehari")
st.pyplot(fig)

### Pola Penyewaan Berdasarkan kategori(Analisis Lanjutan)**
st.subheader("📈 Tren Penyewaan Sepeda Berdasarkan Kategori")
fig, ax = plt.subplots(figsize=(10,5))
sns.countplot(x="usage_category", data=filtered_df, palette="coolwarm")
ax.set_xlabel("Kategori Penggunaan")
ax.set_ylabel("Jumlah Hari")
ax.set_title("Trend Penggunaan Sepeda (Low, Medium, High Usage)")
st.pyplot(fig)

### Pengaruh Cuaca terhadap Penggunaan Sepeda(Analisis Lanjutan)**
st.subheader("🌦 Pengaruh Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x='weathersit_day', y='cnt_day', hue='usage_category', data=filtered_df, palette='coolwarm')
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_title("Pengaruh Cuaca terhadap Penggunaan Sepeda")
st.pyplot(fig)


# Footer
st.caption("Data dari dataset Bike Sharing. Dashboard dibuat oleh Dewi Yuliana 🚀")
