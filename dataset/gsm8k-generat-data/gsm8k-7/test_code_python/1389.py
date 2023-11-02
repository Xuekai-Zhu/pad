def solution():
    words_per_minute_before = 10
    words_per_minute_after = 8
    minutes = 5

    # Calculate the number of words Cameron could type before he broke his arm
    words_before = words_per_minute_before * minutes

    # Calculate the number of words Cameron could type after he broke his arm
    words_after = words_per_minute_after * minutes

    # Calculate the difference between the two
    difference = words_before - words_after
    result = difference
    return result

print(solution())