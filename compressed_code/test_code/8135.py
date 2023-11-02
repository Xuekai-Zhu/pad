def solution():
    
    words_per_minute = 60
    words_to_write = 10800
    minutes_to_write = words_to_write / words_per_minute
    hours_to_write = minutes_to_write / 60
    result = hours_to_write
    return result

print(solution())