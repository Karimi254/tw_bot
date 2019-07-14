#! /usr/bin/python3.6
import tweepy
import logging
from config import create_api
import time 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers.")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()

def fav_rewtweet():
    tweets = api.mentions_timeline()
    for tweet in tweets:
        print(f"Retweeting {tweet.author.name} tweet.")
        tweet.favorite()
        time.sleep(20)
        
def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info('Waiting...')
        time.sleep(60)
if __name__ == "__main__":
    main()

    