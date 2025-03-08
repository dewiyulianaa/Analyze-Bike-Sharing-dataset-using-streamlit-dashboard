import pandas as pd

# Load dataset
day_df = pd.read_csv("https://raw.githubusercontent.com/dewiyulianaa/Analyze-Bike-Sharing-dataset-using-streamlit-dashboard/refs/heads/main/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/dewiyulianaa/Analyze-Bike-Sharing-dataset-using-streamlit-dashboard/refs/heads/main/hour.csv")


# Ubah kolom dteday menjadi tipe datetime agar bisa digabung
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Gabungkan kedua dataset berdasarkan dteday
merged_df = pd.merge(hour_df, day_df, on="dteday", suffixes=("_hour", "_day"))

# Simpan data gabungan ke dalam file CSV
merged_df.to_csv("merged_bike_data.csv", index=False)

print("Dataset berhasil digabung dan disimpan sebagai 'merged_bike_data.csv'")
