import tweepy
from datetime import timedelta, date
import numpy as np

CONSUMER_KEY = "niFysaEmv6CTSrG9pP5IA3QDK"
CONSUMER_SECRET = "i1MFpIFS4SYYllSDMeis9dCk9WudHGB3bF04HJoUqJfH2nGtt6"

auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True, compression = True)

# Get input from user
response = input("Please enter Keyword: ")

print("Fetch twitter data for "+ response + " company keyword....")

keyword = response

start = date(2019, 7, 15)
end = date(2020, 7, 10)
delta = end-start
dateList = []
for i in range(delta.days):
    if (i % 7 != 5) or (i % 7 != 6):
        new_day = start + timedelta(i)
        dateList.append(new_day.strftime("%Y-%m-%d"))

allTweets = []
for i in range(len(dateList)-1):
    dayTweets = []
    results = tweepy.Cursor(api.search, q=keyword, lang="en", since=dateList[i], until=dateList[i+1],
                        result_type="recent", count = 50).items()
    for tweet in results:
        dayTweets.append(tweet.text)
    numpy_array = np.array(dayTweets)
    transpose = numpy_array.T
    allTweets.append(transpose)