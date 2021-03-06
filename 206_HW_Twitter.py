import unittest
import tweepy
import requests
import json
import twitter_info
## SI 206 - HW
## COMMENT WITH: Katarina Mazanka, katmazan
## Your section day/time: Thurs 6-7
## Any names of people you worked with on this assignment:
## add commnet when ad twitter info

## Write code that uses the tweepy library to search for tweets with three different phrases of the 
## user's choice (should use the Python input function), and prints out the Tweet text and the 
## created_at value (note that this will be in GMT time) of the first FIVE tweets with at least 
## 1 blank line in between each of them, e.g.


## You should cache all of the data from this exercise in a file, and submit the cache file 
## along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets 
## about "rock climbing", when we run your code, the code should use CACHED data, and should not 
## need to make any new request to the Twitter API.  But if, for instance, you have never 
## searched for "bicycles" before you submitted your final files, then if we enter "bicycles" 
## when we run your code, it _should_ make a request to the Twitter API.

## Because it is dependent on user input, there are no unit tests for this -- we will 
## run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

##SAMPLE OUTPUT
## See: https://docs.google.com/a/umich.edu/document/d/1o8CWsdO2aRT7iUz9okiCHCVgU5x_FyZkabu2l9qwkf8/edit?usp=sharing



## **** For extra credit, create another file called twitter_info.py that 
## contains your consumer_key, consumer_secret, access_token, and access_token_secret, 
## import that file here.  Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information 
## for an 'extra' Twitter account you make just for this class, and not your personal 
## account, because it's not ideal to share your authentication information for a real 
## account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these 
## with variables rather than filling in the empty strings if you choose to do the secure way 
## for EC points
consumer_key = twitter_info.consumer_key 
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Set up library to grab stuff from twitter with your authentication, and 
# return it in a JSON-formatted way

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())



##creating cache json file
CACHE_FNAME = 'cache.json' # String for your file. We want the JSON file type, bcause that way, we can easily get the information into a Python dictionary!

try:
    cache_file = open(CACHE_FNAME, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION = {}

def gettweets(search):
    
     ##looks for key in dictionary
    if search in CACHE_DICTION:
        print("Data was in the cache")
        print(CACHE_DICTION[search])
        return CACHE_DICTION[search]
    else:
        print("Making a request")
        print("Retrieving" + "\n")
        ##searches for the term in all tweets
        results = api.search(q=search, count = 5)
        ##gets on only the tweets
        list_tweets = results["statuses"]
    

        tweets = " "
        for tweet in list_tweets:
            ##prints the text and the time
            tweets = tweets + ("TEXT: " + tweet["text"] + "\n" + "CREATED AT: " + tweet["created_at"] + "\n" + "\n")
            print(tweets)
        ##adds to the dictionary
        CACHE_DICTION[search] = tweets
            
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return CACHE_DICTION[search]
        

for i in range(0,3):
    search = input("Enter Tweet term: ")
    gettweets(search)
    









