def solution():
    happy_rate = 18
    hungry_rate = 4
    mirror_rate = 45
    happy_time = 20
    hungry_time = 20
    mirror_time = 20

    # Calculate the total number of tweets when Polly is happy
    happy_tweets = happy_rate * happy_time

    # Calculate the total number of tweets when Polly is hungry
    hungry_tweets = hungry_rate * hungry_time

    # Calculate the total number of tweets when Polly is watching herself in the mirror
    mirror_tweets = mirror_rate * mirror_time

    # Calculate the total number of tweets during the whole time period
    total_tweets = happy_tweets + hungry_tweets + mirror_tweets
    result = total_tweets
    return result

print(solution())