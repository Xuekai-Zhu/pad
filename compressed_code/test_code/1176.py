def solution():
    
    hourly_rate = 15
    friday_hours = 10
    saturday_hours = 6
    sunday_hours = 14
    friday_earnings = friday_hours * hourly_rate
    saturday_earnings = saturday_hours * hourly_rate
    sunday_earnings = sunday_hours * hourly_rate
    total_earnings = friday_earnings + saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())