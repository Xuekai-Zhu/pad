def solution():
    
    old_cost_per_day = 0.85
    new_cost_per_day = 0.45
    days_per_month = 30
    old_cost_per_month = old_cost_per_day * days_per_month
    new_cost_per_month = new_cost_per_day * days_per_month
    savings_per_month = old_cost_per_month - new_cost_per_month
    result = savings_per_month
    return result

print(solution())