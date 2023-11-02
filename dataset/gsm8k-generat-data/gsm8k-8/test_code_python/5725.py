def solution():
    # Calculate the number of words Tim learns each year
    words_learned_per_year = 10 * 365

    # Calculate the total number of words he learned in 2 years
    total_words_learned = words_learned_per_year * 2

    # Calculate the percentage increase in his vocabulary
    percent_increase = 50

    # Calculate the original number of words he knew
    original_words = total_words_learned / (percent_increase/100 + 1)
    result = original_words
    return result

print(solution())