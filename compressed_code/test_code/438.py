def solution():
    
    min_daily_veggies = 2
    total_veggies_consumed = 8
    remaining_veggies = min_daily_veggies * 7 - total_veggies_consumed
    days_left_in_week = 7 - 5  
    cups_per_day = remaining_veggies / days_left_in_week
    result = cups_per_day
    return result

print(solution())