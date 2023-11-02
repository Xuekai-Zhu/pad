def solution():
    
    words_per_minute = 50
    minutes_per_hour = 60
    hours_per_day = 4
    days = 7
    total_minutes = minutes_per_hour * hours_per_day * days
    total_words = words_per_minute * total_minutes
    result = total_words
    return result

print(solution())