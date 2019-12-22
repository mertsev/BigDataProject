import praw
import requests
import requests.auth
import json

from datetime import datetime
from pandas import DataFrame

username = 'bigdatasmallpeepee'
password = 'Qazxswedc1'
secret = 'fI0dqVLaJPsOC86crfkRmKCZ40E'
client_id = 'cjwu3FA4Mn03Sg'

reddit = praw.Reddit(user_agent='Comment Extraction (by /u/BigDataProject)',
                     client_id=client_id, client_secret=secret,
                     username=username, password=password)

#Display the submissions of the last 24 hours in /r/all.
lastday_subreddit = reddit.subreddit('starwars').top('day',limit=2000)
subreddits = set()
count = 0;
for submission in lastday_subreddit:
    subreddits.add(submission.subreddit.display_name)
    count+=1
    print(submission.title)
    #print(20*'-')
    #print(submission.subreddit.display_name)

print(len(subreddits))
print(subreddits)