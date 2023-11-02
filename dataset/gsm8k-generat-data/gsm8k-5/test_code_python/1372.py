def solution():
    micah_speed = 20  # Micah can type 20 words per minute
    isaiah_speed = 40  # Isaiah can type 40 words per minute
    minutes_per_hour = 60  # There are 60 minutes in an hour

    # Calculate the total number of words Micah can type in an hour
    micah_words_per_hour = micah_speed * minutes_per_hour

    # Calculate the total number of words Isaiah can type in an hour
    isaiah_words_per_hour = isaiah_speed * minutes_per_hour

    # Calculate the difference in the number of words that Isaiah and Micah can type in an hour
    words_difference = isaiah_words_per_hour - micah_words_per_hour
    result = words_difference
    return result

print(solution())