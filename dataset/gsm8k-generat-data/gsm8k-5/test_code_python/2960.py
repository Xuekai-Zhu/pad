def solution():
    words_per_minute = 60  # Emily types 60 words per minute
    words_to_write = 10800  # Emily wants to write 10,800 words

    # Calculate the time it takes Emily to write the required number of words
    minutes_taken = words_to_write / words_per_minute
    hours_taken = minutes_taken / 60
    result = hours_taken
    return result

print(solution())