def solution():
    """Before Cameron broke his right arm, he was able to type 10 words per minute on his phone. After he broke his arm, he had to use his left hand for a while, and he could only type 8 words per minute. What is the difference between the number of words he could type in 5 minutes before and after he broke his arm?"""
    # Define the typing speed before and after the injury
    speed_before = 10
    speed_after = 8

    # Define the time period
    time_period = 5

    # Calculate the number of words typed before and after the injury
    words_before = speed_before * time_period
    words_after = speed_after * time_period

    # Calculate the difference
    difference = words_before - words_after

    # Return the result
    result = difference
    return result

print(solution())