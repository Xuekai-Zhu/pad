def solution():
    
    hourly_rate = 8
    hours_per_week = 35
    weeks_per_month = 4
    total_earned = hourly_rate * hours_per_week * weeks_per_month
    bike_cost = 400
    money_left = total_earned - bike_cost
    result = money_left
    return result

print(solution())