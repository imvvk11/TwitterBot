
#import tweepy library
import tweepy
from time import sleep


consumer_key='your consumer key'
consumer_secret='your consumer secret'
access_token='your access token'
access_token_secret='your access secret'
# Access and authorize Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open text file verne.txt (or your chosen file) for reading
my_file = open('verne.txt', 'r')

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

#uncomment below lines to tweet from reading the text file
"""def tweet():
    for line in file_lines:
        try:
             print(line)
             if line != '\n':
                 api.update_status(line)
                 sleep(50)
             else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)
tweet()
"""

#wrrite any trending topics in tweepy.Cursor(api.search, q='#FuelChallenge')
q='#topicname'
for tweet in tweepy.Cursor(api.search, q='#FuelChallenge').items():
    # Add try ... except block to catch and output errorstweet()
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')




        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        #Follow the user who tweeted
        if not tweet.user.following:
            tweet.user.follow()
            print('Followed the user')

        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break


