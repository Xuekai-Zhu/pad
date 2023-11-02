def solution():
    
    total_words = 200 + 400 + 300
    hours_to_read = total_words / 100
    minutes_to_read = hours_to_read * 60
    days_to_read = 10
    minutes_per_day = minutes_to_read / days_to_read
    result = minutes_per_day
    return result

print(solution())