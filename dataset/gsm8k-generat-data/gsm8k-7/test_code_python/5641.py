def solution():
    total_words = 1200
    words_per_hour_1 = 400
    hours_1 = 2
    words_per_hour_2 = 200

    # Calculate the total words written during the first two hours
    words_written_1 = words_per_hour_1 * hours_1

    # Calculate the remaining words that need to be written
    remaining_words = total_words - words_written_1

    # Calculate the time needed to write the remaining words
    hours_2 = remaining_words / words_per_hour_2

    # Calculate the total time needed to finish the essay
    total_hours = hours_1 + hours_2
    result = total_hours
    return result

print(solution())