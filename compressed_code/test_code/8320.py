def solution():
    
    current_rate = 16
    new_rate = 12
    extra_charge = 3
    hours_per_day = 6
    screams_per_day = 2
    current_cost = current_rate * hours_per_day
    new_cost = new_rate * hours_per_day + screams_per_day * extra_charge
    savings_per_day = current_cost - new_cost
    result = savings_per_day
    return result

print(solution())