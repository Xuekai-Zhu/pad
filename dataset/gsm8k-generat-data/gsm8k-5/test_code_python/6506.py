def solution():
    happy_tweets_per_minute = 18
    hungry_tweets_per_minute = 4
    mirror_tweets_per_minute = 45

    # Calculate the total number of tweets from each activity
    happy_tweets = happy_tweets_per_minute * 20
    hungry_tweets = hungry_tweets_per_minute * 20
    mirror_tweets = mirror_tweets_per_minute * 20

    # Calculate the total number of tweets in the 1-hour period
    total_tweets = happy_tweets + hungry_tweets + mirror_tweets
    result = total_tweets
    return result

print(solution())