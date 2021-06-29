import tweepy
import logging
import time
import re

class MyStreamListener(tweepy.StreamListener):

        def on_status(self, status):
            print("Status Text: "+ status.text + " Status ID: "+ str(status.id) + " Status User: " + status.user.screen_name)
            tweetid=status.id
            screenName = status.user.screen_name
            text = status.text
            BotID = 1171125140459053057
            print("User who responded to us: " +screenName)
            print("this is text: " + text)
            print(type(text))

            words = ('HELP' or 'DM')

            if(screenName == "DankRedditBot"):
                print("**** This is the bot replying, stopping further communications ****")
            else:
                if('HELP' in text.upper()):
                    print("Contains Key Words, sending response.")
                    api.update_status(status= "@"+ screenName + " Hello! Please Send a Dm to @JustASuspect for any help or complaints!",in_reply_to_status_id = tweetid)
                elif('DM' in text.upper()):
                    print("Contains Key Words, sending response.")
                    api.update_status(status= "@"+ screenName + " Hello! Please Send a Dm to @JustASuspect for any help or complaints!",in_reply_to_status_id = tweetid)
                else:
                    print("Does not contain Key Words")



# Authenticate to Twitter
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("",
                      "")

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("*Authentication OK*")
except:
    print("Error during authentication")

api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth= api.auth, listener=myStreamListener)
print("Stream Created")

myStream.filter(follow=["1171125140459053057"],is_async=True)
