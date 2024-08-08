import pandas as pd
import matplotlib.pyplot as plt

# Memuat data dari file CSV
file_path = '../Data Film Deadpool And Wolverine.csv'  # Ganti dengan path file CSV Anda
data = pd.read_csv(file_path)

# Menghapus baris dengan nilai NaN di kolom 'clean_tweet'
data = data.dropna(subset=['clean_tweet'])

# Kata-kata yang akan dihitung frekuensinya
words_to_count = ["terbaik", "seru", "bagus", "keren", "epic", "mengagumkan"]

# Menghitung frekuensi kata-kata
word_counts = {word: 0 for word in words_to_count}
for tweet in data['clean_tweet']:
    if isinstance(tweet, str):
        for word in words_to_count:
            word_counts[word] += tweet.split().count(word)

# Membuat DataFrame dari hasil hitungan kata
word_count_df = pd.DataFrame(list(word_counts.items()), columns=['word', 'count'])

# Menampilkan DataFrame untuk memastikan hasil
print(word_count_df)

# Membuat grafik batang untuk frekuensi kata-kata
plt.figure(figsize=(10, 6))
plt.bar(word_count_df['word'], word_count_df['count'], color='skyblue')
plt.title('Frekuensi Kata-kata dalam Tweet')
plt.xlabel('Kata')
plt.ylabel('Jumlah')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Menampilkan grafik
plt.show()
