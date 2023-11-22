def solution():
    
    hourly_rate = 10
    first_week_hours = 5
    second_week_hours = 8
    first_week_earnings = first_week_hours * hourly_rate
    second_week_earnings = second_week_hours * hourly_rate
    total_earnings = first_week_earnings + second_week_earnings
    result = total_earnings
    return result

print(solution())