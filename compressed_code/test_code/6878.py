def solution():
    
    words_per_minute_before = 10
    words_per_minute_after = 8
    time_in_minutes = 5
    words_before = words_per_minute_before * time_in_minutes
    words_after = words_per_minute_after * time_in_minutes
    difference = words_before - words_after
    result = difference
    return result

print(solution())