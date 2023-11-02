def solution():
    words_per_minute_micah = 20
    words_per_minute_isaiah = 40
    minutes_in_an_hour = 60
    total_words_micah = words_per_minute_micah * minutes_in_an_hour
    total_words_isaiah = words_per_minute_isaiah * minutes_in_an_hour
    result = total_words_isaiah - total_words_micah
    return result

print(solution())