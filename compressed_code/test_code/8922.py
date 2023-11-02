def solution():
    
    daily_reading_rate = 50 * 2 
    days_to_complete = 2800 / daily_reading_rate 
    weeks_to_complete = days_to_complete / 7 
    result = weeks_to_complete
    return result

print(solution())