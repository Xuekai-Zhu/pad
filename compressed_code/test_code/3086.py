def solution():
    
    daily_reading_time = 2  
    reading_rate = 50  
    bible_length = 2800  
    daily_reading_progress = daily_reading_time * reading_rate
    total_days = bible_length // daily_reading_progress
    weeks = total_days // 7
    result = weeks
    return result

print(solution())