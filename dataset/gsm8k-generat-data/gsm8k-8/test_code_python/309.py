def solution():
    # Calculate the total minutes Carl types in a day
    minutes_per_day = 4 * 60

    # Calculate the total words Carl can type in a day
    words_per_day = minutes_per_day * 50

    # Calculate the total words Carl can type in 7 days
    total_words = words_per_day * 7
    result = total_words
    return result

print(solution())