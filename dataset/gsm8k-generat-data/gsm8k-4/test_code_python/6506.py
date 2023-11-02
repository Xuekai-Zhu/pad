def solution():
    """Polly the parakeet tweets all day long. When she is happy, she tweets 18 times per minute. When she is hungry, she tweets 4 times per minute. And when she watches herself in the mirror, she tweets 45 times per minute. During a time period where she is happy for 20 minutes, hungry for 20 minutes, and watches her reflection for 20 minutes, what is the total number of times she will tweet?"""
    # Define the number of minutes Polly spends happy, hungry, and watching herself in the mirror
    happy_minutes = 20
    hungry_minutes = 20
    mirror_minutes = 20

    # Define the number of tweets per minute when Polly is happy, hungry, and watching herself in the mirror
    happy_tweets_per_minute = 18
    hungry_tweets_per_minute = 4
    mirror_tweets_per_minute = 45

    # Calculate the total number of tweets Polly makes during each period
    happy_tweets = happy_minutes * happy_tweets_per_minute
    hungry_tweets = hungry_minutes * hungry_tweets_per_minute
    mirror_tweets = mirror_minutes * mirror_tweets_per_minute

    # Calculate the total number of tweets Polly makes during the entire time period
    total_tweets = happy_tweets + hungry_tweets + mirror_tweets

    result = total_tweets
    return result

print(solution())