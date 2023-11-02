def solution():
    words_learned_per_day = 10
    days_in_2_years = 2 * 365  # assuming no leap year

    # Calculate the number of words Tim learned in 2 years
    words_learned_in_2_years = words_learned_per_day * days_in_2_years

    # Calculate the total number of words Tim knows after the book increased his vocabulary by 50%
    total_words_after_increase = words_learned_in_2_years * 1.5

    # Calculate how many words Tim knew originally
    original_words = total_words_after_increase - words_learned_in_2_years
    result = original_words
    return result

print(solution())