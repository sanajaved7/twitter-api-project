from TwitterAPI import TwitterAPI
import csv
from config import (consumer_key, consumer_secret,
                    access_token_key, access_token_secret)

api = TwitterAPI(consumer_key, consumer_secret,
                 access_token_key, access_token_secret)


def twitter_search(twitter_query):
    """ Pass in what you want to search for in
    Twitter and it creates a csv file with
    the tweets pulled from the API
    """
    request_tweets = api.request('search/tweets', {'q': twitter_query})
    return request_tweets


def prepare_tweets(tweet):
    """ Pass in tweet and returns list of elements of
    each tweet for csv or other destination"""
    return [
        tweet["text"],
        tweet["retweet_count"],
        tweet["user"]["name"],
        tweet["favorite_count"],
        tweet["user"]["location"],
        tweet["created_at"],
        hashtags(tweet["entities"]["hashtags"])
    ]


def make_csv(request_tweets):
    with open('twitterproj.csv', 'w') as csvfile:
        twitter_writer = csv.writer(csvfile)
        twitter_writer.writerow([
            "Tweet Text",
            "Number of Retweets",
            "User Name",
            "Number of Favorites",
            "Location of User",
            "Date/Time of Tweet",
            "Hashtags in Tweet"])
        for tweet in request_tweets:
            twitter_writer.writerow(prepare_tweets(tweet))


def hashtags(list_of_hashtags):
    string = ""
    for x in list_of_hashtags:
        string += "#" + x["text"] + " "
    return string

# "text"
# "retweet_count"
# "user"
# "favourites_count"
# "location"
# "created_at"
# "hashtags"

if __name__ == '__main__':
    tweets = twitter_search("#blacklivesmatter")
    make_csv(tweets)
    # get twitter search , etc
    # some_fucntion_that_processes_raw_input()
