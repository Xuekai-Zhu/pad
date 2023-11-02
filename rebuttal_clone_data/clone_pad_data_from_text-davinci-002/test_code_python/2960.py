def solution():
    words_per_minute = 60
    total_words = 10800
    minutes_per_hour = 60
    words_per_hour = words_per_minute * minutes_per_hour
    total_hours = total_words / words_per_hour
    result = total_hours
    return result

print(solution())