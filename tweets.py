from TwitterAPI import TwitterAPI
import csv
from config import consumer_key, consumer_secret, access_token_key, access_token_secret

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)


request_tweets = api.request('search/tweets', {'q':'#blacklivesmatter'})

def hashtags(list_of_hashtags):
    string = ""
    for x in list_of_hashtags:
        string += "#" + x["text"] + " "
    return string

with open('twitterproj.csv', 'w') as csvfile:
    twitter_writer = csv.writer(csvfile)
    twitter_writer.writerow(
        ["Tweet Text",
        "Number of Retweets",
        "User Name",
        "Number of Favorites",
        "Location of User",
        "Date/Time of Tweet",
        "Hashtags in Tweet"])
    for item in request_tweets:
         twitter_writer.writerow([
            item["text"],
            item["retweet_count"],
            item["user"]["name"],
            item["favorite_count"],
            item["user"]["location"],
            item["created_at"],
            hashtags(item["entities"]["hashtags"])
        ])

# "text"
# "retweet_count"
# "user"
# "favourites_count"
# "location"
# "created_at"
# "hashtags"
