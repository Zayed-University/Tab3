import time
import tweepy #tweepy is an open-sourced twitter library that enables access to Twitter API through Python

#credentials to use Twitter API (gotten from Twitter)

consumer_key = 'FXKvw4G8T7WvcDJVRC3idu9GF'
consumer_secret = 'FjiCUFWCIHDpw5uyz7wKfKIpJt7raJbB9RAlwbIeeq330LAOyy'
access_key = '798537242989985796-7yahqRkAgiv6ri4OOpWygaAay09hWuN'
access_secret = 'ZH0ZAATeLjllcSVprd7rY0k3si4mWRyKGgqyLBBqaPCHT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

results = api.search(q="Abu Dhabi Art", count=100) #count is used for number of results

for result in results:
    print result.text
    time.sleep(30) #time.sleep is used for seconds between each tweet result
