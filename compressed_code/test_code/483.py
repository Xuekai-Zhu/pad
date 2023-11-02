def solution():
    
    charge_cost = 3.5
    num_charges = 4
    charging_budget = 20
    total_charge_cost = charge_cost * num_charges
    money_left = charging_budget - total_charge_cost
    result = money_left
    return result

print(solution())