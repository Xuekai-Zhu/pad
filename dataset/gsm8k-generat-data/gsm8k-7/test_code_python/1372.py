def solution():
    words_per_minute_micah = 20
    words_per_minute_isaiah = 40
    minutes_per_hour = 60

    # Calculate the number of words Micah can type in an hour
    words_per_hour_micah = words_per_minute_micah * minutes_per_hour

    # Calculate the number of words Isaiah can type in an hour
    words_per_hour_isaiah = words_per_minute_isaiah * minutes_per_hour

    # Calculate the difference in the number of words Isaiah can type and Micah can type in an hour
    diff_words_per_hour = words_per_hour_isaiah - words_per_hour_micah
    result = diff_words_per_hour
    return result

print(solution())