def solution():
    """Sandy earns $15 per hour. She worked 10 hours on Friday with her best friend, 6 hours on Saturday alone and 14 hours on Sunday with her other co-workers. How much money did Sandy earn in all on Friday, Saturday and Sunday?"""
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