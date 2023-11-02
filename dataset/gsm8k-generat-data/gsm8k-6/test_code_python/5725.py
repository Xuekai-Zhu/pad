def solution():
    # Calculate the total number of words Tim learned in 2 years
    words_learned = 10 * 365 * 2  # Tim learns 10 words from the book each day for 2 years
    # Calculate the percentage increase in words known
    percentage_increase = 50 / 100
    # Calculate the original number of words
    original_words = words_learned / (1 + percentage_increase)
    result = original_words
    return result

print(solution())