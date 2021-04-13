import tweepy

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECERET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECERET)
api = tweepy.API(auth)

count = 20
result_type = "recent"
screen_name = ""

print("screen_name={}, result_type={}, count={}".format(
    screen_name, result_type, count))
results = api.user_timeline(screen_name=screen_name,
                            result_type=result_type, count=count)
for status in results:
    tweet_id = status.id
    print(screen_name, tweet_id, status.entities["urls"])
    try:
        if not "RT @" in status.text[0:4]:
            print("Like!")
            api.create_favorite(tweet_id)
    except:
        pass
