#!/usr/bin/env python3

import tweepy
import pprint
import datetime
import pytz

CONSUMER_KEY = "e2Hqw5TgDc8EUsA0RmP8XBJMj"
CONSUMER_SECRET_KEY = "5NxskZP7t46UfI6Gwi5hdrIbJRtX0NDmCEWtT1evAzFuoC3PNj"

ACCESS_TOKEN = "1345949283745411072-9vmNSqlxRSIPJ61qNVZv6Dko1vLNql"
ACCESS_TOKEN_SECRET = "KD6cbo7xColK3pps0wV4llYuex3BK8Fa7u1tqyTduxchr"

SEARS_USERNAME = "searysears"

CURRENT_TIME = datetime.datetime.utcnow()

def retrieve_timeline( api, user ):
    return api.user_timeline(screen_name = user, include_rts = True)


def main():
    # create authenticator
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # create api object
    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

    # grab current timeline
    sears_tweets = retrieve_timeline(api, SEARS_USERNAME)
    
    # run through tweets and retweets
    for tweet in sears_tweets:
        time_obj = datetime.datetime.strptime(tweet._json['created_at'][4:],"%b %d %H:%M:%S %z %Y" )
        if "RT" in tweet._json['text']:
            print(f"{tweet._json['user']['name']} retweeted {tweet._json['text'][2:]} at {tweet._json['created_at']}")
        else:
            print(f"{tweet._json['user']['name']} tweeted {tweet._json['text']} at {tweet._json['created_at']}")




if __name__ == "__main__":
    main()
