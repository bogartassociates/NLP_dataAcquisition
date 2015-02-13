#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import pymongo
import tweepy

#get your own keys!

consumer_key = "yourConsumerKey"
consumer_secret = "yourConsumerSecret"
access_key = "yourAccessKey"
access_secret = "yourAccessSecret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        self.db = pymongo.MongoClient().twitter

    def on_data(self, tweet):
        self.db.tweets.insert(json.loads(tweet))

    def on_error(self, status_code):
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream


sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))

#Middle East (Levant/Arabian Peninsula)
sapi.filter(locations=[12.254843, 34.471938, 38.303034, 51.908570])
