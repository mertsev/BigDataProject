import praw
import requests
import requests.auth
import json
import sys

from datetime import datetime
from pandas import DataFrame
from praw.models import MoreComments

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

def word_count(text):
    for char in '-.,\n':
        text=text.replace(char,' ')
    text = text.lower()
    # split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s) 
    word_list = text.split()
    return len(word_list)

subredditList = reddit.user.subreddits(limit=None)

subreddits = []
for item in subredditList:
    subreddits.append(item.display_name)
    print(item.display_name)

i = 0

lastday_subreddit = reddit.subreddit('all').top('day',limit=2000)
subreddits_set = set()
for submission in lastday_subreddit:
    subreddits_set.add(submission.subreddit.display_name)
    print(submission.subreddit.display_name)

subreddits = subreddits + list(subreddits_set)

for subreddit in subreddits:
    print(subreddit)

for subreddit in subreddits_set:
    data = {}
    titles = []
    texts = []
    texts_word_count = []
    texts_letter_count = []
    comments = []
    links = []
    upvote_ratio = []
    upvote_score = []
    num_comments = []
    authors_comment_karma = []
    authors_link_karma = []
    created_date = []
    for submission in reddit.subreddit(subreddit).hot(limit=1):
        try:
            print("Subreddit: " + subreddit)
            title = str(submission.title)
            print(str(i) + ' ' + title)
            titles.append(title)

            selftext = submission.selftext.replace(',',' ')
            texts.append(selftext)
            texts_letter_count.append(len(selftext))
            texts_word_count.append(word_count(selftext))
            
            comment_text = ""
            for top_level_comment in submission.comments:
                if isinstance(top_level_comment, MoreComments):
                    continue
                comment_text += top_level_comment.body
            comments.append(comment_text)
            links.append(submission.link_flair_text)
            upvote_ratio.append(submission.upvote_ratio)
            num_comments.append(submission.num_comments)
            upvote_score.append(submission.score)
            # redditor = submission.author
            # authors_comment_karma.append(redditor.comment_karma)
            # authors_link_karma.append(redditor.link_karma)
            created_date.append(datetime.utcfromtimestamp(submission.created_utc))
        except: 
            e = sys.exc_info()[0]
            print(e)
    i = i + 1

    # заглавие сабмишена
    data["title"] = titles
    # основной текст
    data["text"] = texts
    # количество слов
    data["words_count"] = texts_word_count
    # количество символов
    data["letters_count"] = texts_letter_count
    # слепленный текст всех топ-комментов
    data["comment_text"] = comments
    # бирка (Discussion, Review и тд)
    data["link"] = links
    # доля апвоутящих
    data["upvote_ratio"] = upvote_ratio
    # сколько апвоутящих
    data["upvote_score"] = upvote_score
    # количество комментов
    data["num_comments"] = num_comments
    # коммент карма автора
    # data["comment_karma"] = authors_comment_karma
    # ??? линк карма автора
    # data["link_karma"] = authors_link_karma
    # дата создания сабмишена
    data["created_date"] = created_date

    df = DataFrame(data)
    print(df)
    df.to_parquet('testdata/' + subreddit + '_reddit_data.parquet')