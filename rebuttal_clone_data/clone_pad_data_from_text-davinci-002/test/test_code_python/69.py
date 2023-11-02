def solution():
    
    hourly_wage = 8
    hours_worked = 35
    weeks_worked = 4
    total_hours = hours_worked * weeks_worked
    total_wage = hourly_wage * total_hours
    bike_cost = 400
    money_left = total_wage - bike_cost
    result = money_left
    return result

print(solution())