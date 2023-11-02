def solution():
    # Calculate the number of words Cameron could type before he broke his arm
    words_before_break = 10 * 5  # 10 words per minute, for 5 minutes

    # Calculate the number of words Cameron could type after he broke his arm
    words_after_break = 8 * 5  # 8 words per minute, for 5 minutes

    # Calculate the difference in the number of words typed before and after the arm break
    difference = words_before_break - words_after_break
    result = difference
    return result

print(solution())