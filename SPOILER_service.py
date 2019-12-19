import praw
import requests
import requests.auth
import json

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

for submission in reddit.subreddit('Amd').hot(limit=25):
    print('--------------------')
    print(submission.title)

# for submission in reddit.front.hot(limit=5):
#     # print('--------------------------')
#     print('Title: ' + str(submission.title))
#     print('Permalink: ' + str(submission.permalink))
#     print('Upvote: ' + str(submission.upvote_ratio))
#     redditor = submission.author
#     print('Author: ' + str(redditor) + '; Comments: ' + str(submission.num_comments))
#     print('Author karma: ' + str(redditor.comment_karma))
#     print('--------------------------')
    # for top_level_comment in submission.comments:
        # print(top_level_comment.body)
