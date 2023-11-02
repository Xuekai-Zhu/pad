def solution():
    
    hourly_rate = 15
    friday_hours = 10
    saturday_hours = 6
    sunday_hours = 14
    friday_earnings = hourly_rate * friday_hours
    saturday_earnings = hourly_rate * saturday_hours
    sunday_earnings = hourly_rate * sunday_hours
    total_earnings = friday_earnings + saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())