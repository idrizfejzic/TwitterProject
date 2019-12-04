import os
import tweepy as tw
import pandas as pd

consumer_key= 'XBuKrGqxjQBWp2XOcdwGZLzcg'
consumer_secret= 'tVdKxqrU16TJHUcEhQZnofAt6rSSuk7oCss8yjnJw6KRGUj6SU'
access_token= '370140893-87zTUu8DCcMXzeGJ2z7gQwwRXIJXlZuRm2POa7kv'
access_token_secret= '4D4H7iyols9M8XVy8nbo0K0YqKPsM5K3YJLPv9MKycNbT'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

trends1 = api.trends_place(1) # from the end of your code
# trends1 is a list with only one element in it, which is a 
# dict which we'll put in data.
data = trends1[0] 
# grab the trends
trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them
trendsName = ' '.join(names)
print(trendsName)
