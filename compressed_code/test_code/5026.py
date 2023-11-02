def solution():
    
    happy_tweets_per_minute = 18
    hungry_tweets_per_minute = 4
    mirror_tweets_per_minute = 45

    happy_tweet_total = happy_tweets_per_minute * 20
    hungry_tweet_total = hungry_tweets_per_minute * 20
    mirror_tweet_total = mirror_tweets_per_minute * 20

    total_tweets = happy_tweet_total + hungry_tweet_total + mirror_tweet_total
    result = total_tweets
    return result

print(solution())