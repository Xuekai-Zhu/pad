def solution():
    happy_tweets_per_minute = 18
    hungry_tweets_per_minute = 4
    watch_tweets_per_minute = 45
    happy_minutes = 20
    hungry_minutes = 20
    watch_minutes = 20
    happy_tweets = happy_tweets_per_minute * happy_minutes
    hungry_tweets = hungry_tweets_per_minute * hungry_minutes
    watch_tweets = watch_tweets_per_minute * watch_minutes
    total_tweets = happy_tweets + hungry_tweets + watch_tweets
    result = total_tweets
    return result

print(solution())