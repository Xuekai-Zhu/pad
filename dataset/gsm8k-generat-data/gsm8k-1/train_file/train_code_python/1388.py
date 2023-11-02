def solution():
    """Before Cameron broke his right arm, he was able to type 10 words per minute on his phone. After he broke his arm, he had to use his left hand for a while, and he could only type 8 words per minute. What is the difference between the number of words he could type in 5 minutes before and after he broke his arm?"""
    words_per_minute_before = 10
    words_per_minute_after = 8
    time_in_minutes = 5
    words_before = words_per_minute_before * time_in_minutes
    words_after = words_per_minute_after * time_in_minutes
    difference = words_before - words_after
    result = difference
    return result

print(solution())