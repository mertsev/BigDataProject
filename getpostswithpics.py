# ЭТО ПРОСТО КАЧАЕТ МЕМЫ, СЕРЁЖА ЭТО ЗОЛОТАЯ ЖИЛА!

import praw
import requests
import requests.auth
import json

import urllib.request as req

username = 'bigdatasmallpeepee'
password = 'Qazxswedc1'
secret = 'fI0dqVLaJPsOC86crfkRmKCZ40E'
client_id = 'cjwu3FA4Mn03Sg'

# client_auth = requests.auth.HTTPBasicAuth(client_id, secret)
# post_data = {"grant_type": "password", "username": username, "password": password}
# headers = {"User-Agent": "ChangeMeClient/0.1 by " + username}
# response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

# print(response.json())
# token = '366796926589-aD_104VknNfc-rVZ8ig6O45E_go'

reddit = praw.Reddit(user_agent='Comment Extraction (by /u/BigDataProject)',
                     client_id=client_id, client_secret=secret,
                     username=username, password=password)


subreddit = 'memes'

i = 0
for post in reddit.subreddit(subreddit).top():
    print(post.url)
    imgurl = post.url
    req.urlretrieve(imgurl, "memes/" + str(i) + ".jpg")
    i += 1