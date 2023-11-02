def solution():
    
    old_refrigerator_cost_per_day = 0.85
    new_refrigerator_cost_per_day = 0.45
    days_in_month = 30
    old_refrigerator_cost_per_month = old_refrigerator_cost_per_day * days_in_month
    new_refrigerator_cost_per_month = new_refrigerator_cost_per_day * days_in_month
    cost_saved_per_month = old_refrigerator_cost_per_month - new_refrigerator_cost_per_month
    result = cost_saved_per_month
    return result

print(solution())