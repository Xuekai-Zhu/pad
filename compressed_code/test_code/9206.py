def solution():
    
    hours_per_day = 2
    days_worked = 4
    wage_per_hour = 22
    total_wage = hours_per_day * days_worked * wage_per_hour
    supply_cost = 54
    profit = total_wage - supply_cost
    result = profit
    return result

print(solution())