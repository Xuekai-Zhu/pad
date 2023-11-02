def solution():
    
    battery_charges = 4
    cost_per_charge = 3.5
    battery_charging_budget = 20
    total_charging_cost = battery_charges * cost_per_charge
    remaining_money = battery_charging_budget - total_charging_cost
    result = remaining_money
    return result

print(solution())