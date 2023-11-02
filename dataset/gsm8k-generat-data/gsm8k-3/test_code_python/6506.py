def solution():
    """Polly the parakeet tweets all day long.  When she is happy, she tweets 18 times per minute.  When she is hungry, she tweets 4 times per minute.  And when she watches herself in the mirror, she tweets 45 times per minute.  During a time period where she is happy for 20 minutes, hungry for 20 minutes, and watches her reflection for 20 minutes, what is the total number of times she will tweet?"""
    # Define the rate of tweeting for each mood
    HAPPY_RATE = 18
    HUNGRY_RATE = 4
    MIRROR_RATE = 45

    # Define the time period for each mood
    happy_time = 20
    hungry_time = 20
    mirror_time = 20

    # Calculate the total number of tweets
    total_tweets = happy_time * HAPPY_RATE + hungry_time * HUNGRY_RATE + mirror_time * MIRROR_RATE

    # Display the total number of tweets
    result = total_tweets
    return result

print(solution())