def solution():
    
    daily_commute = 1  
    weekend_drive = 2 * 2  
    weekly_drive = daily_commute * 5 + weekend_drive
    result = weekly_drive
    return result

print(solution())