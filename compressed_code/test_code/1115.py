def solution():
    
    total_words = 200 + 400 + 300
    total_hours = total_words / 100
    days = 10
    minutes_per_day = total_hours / days * 60
    result = minutes_per_day
    return result

print(solution())