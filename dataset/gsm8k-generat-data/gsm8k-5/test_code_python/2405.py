def solution():
    words_per_minute = 15  # Lily types 15 words per minute
    break_time = 2  # Lily takes a 2-minute break every 10 minutes
    words_per_set = 150  # Lily types 150 words in every set of 10 minutes
    total_words = 255  # Lily wants to type 255 words

    # Calculate the number of sets of 10 minutes Lily will need to type 255 words
    sets_needed = total_words // words_per_set
    if total_words % words_per_set != 0:
        sets_needed += 1

    # Calculate the total time Lily will need, accounting for breaks
    total_time = sets_needed * 10 + break_time * (sets_needed - 1)

    # Calculate the time it takes to type the remaining words in the last set
    remaining_words = total_words % words_per_set
    time_for_remaining_words = remaining_words / words_per_minute

    # Calculate the total time needed, including the time for the remaining words
    total_time += time_for_remaining_words
    result = total_time
    return result

print(solution())