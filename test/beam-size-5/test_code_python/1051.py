def solution():
    
    normal_cost = 120
    increase_percent = 60
    increase_amount = normal_cost * (increase_percent / 100)
    total_cost_per_month = normal_cost + increase_amount
    total_cost_per_year = total_cost_per_month * 12
    result = total_cost_per_year
    return result

print(solution())