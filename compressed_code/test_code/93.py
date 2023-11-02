def solution():
    
    hourly_rate = 8
    hours_per_week = 35
    weeks_in_month = 4
    total_earnings = hourly_rate * hours_per_week * weeks_in_month
    bike_cost = 400
    money_left_over = total_earnings - bike_cost
    result = money_left_over
    return result

print(solution())