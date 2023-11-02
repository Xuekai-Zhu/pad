def solution():
    words_per_minute = 38
    total_words = 4560

    # Calculate the number of minutes needed to type all the words
    minutes_needed = total_words / words_per_minute

    # Calculate the number of hours needed to type all the words
    hours_needed = minutes_needed / 60
    result = hours_needed
    return result

print(solution())