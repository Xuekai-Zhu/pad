def solution():
    # Calculate the total number of tweets Polly will make in 60 minutes
    happy_tweets = 18 * 20  # 18 tweets per minute for 20 minutes
    hungry_tweets = 4 * 20  # 4 tweets per minute for 20 minutes
    mirror_tweets = 45 * 20  # 45 tweets per minute for 20 minutes
    total_tweets = happy_tweets + hungry_tweets + mirror_tweets

    result = total_tweets
    return result

print(solution())