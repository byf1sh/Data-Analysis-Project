import pandas as pd
import matplotlib.pyplot as plt

# Memuat data dari file CSV
data = pd.read_csv('../Data Film Deadpool And Wolverine.csv')

# Menampilkan beberapa baris pertama data untuk memastikan data dimuat dengan benar
print(data.head())

# Membuat grafik batang untuk distribusi sentimen
sentiment_counts = data['sentiment'].value_counts()
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color=['green', 'blue', 'red'])
plt.title('Distribusi Sentimen')
plt.xlabel('Sentimen')
plt.ylabel('Jumlah Tweet')
plt.xticks(rotation=0)
plt.grid(axis='y')

# Menampilkan grafik
plt.show()
