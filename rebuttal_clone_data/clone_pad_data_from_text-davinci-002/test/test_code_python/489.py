def solution():
    old_fridge_cost = 0.85
    new_fridge_cost = 0.45
    days_in_month = 30
    savings = (old_fridge_cost - new_fridge_cost) * days_in_month
    result = savings
    return result

print(solution())