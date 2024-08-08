import tweepy

# Masukkan kunci dan token API Anda
consumer_key = '4kecH2pe2nHE48L6YMUiuWgK3'
consumer_secret = 'QKWqWs3QpOnwcQVYRPh5VMvgpY1IDjSb7sekVp80FHK52MYg3Y'
access_token = '1271513696-EY7hyrqQdDrCaIN8PhzC7LNtzfvDih4V7iI96Jp'
access_token_secret = 'lHfQJ9GDI6NbcXgR7EF2384c7iz1YXtqaWi2370EfXNyQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Mengumpulkan tweet berdasarkan hashtag
hashtag = "#ProdukBaru"
tweets = tweepy.Cursor(api.search_tweets, q=hashtag, lang="id", tweet_mode='extended').items(1000)

# Menyimpan tweet dalam daftar
tweet_data = []
for tweet in tweets:
    tweet_data.append(tweet.full_text)

print("Jumlah tweet yang dikumpulkan:", len(tweet_data))