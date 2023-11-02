def solution():
    """Hawkeye is driving to his aunt. He has to charge his battery for $3.5 per charge. If he charged his battery four times, and his battery charging budget was $20, how much money was he left with when he reached his aunt's place?"""
    battery_charges = 4
    cost_per_charge = 3.5
    battery_charging_budget = 20
    total_charging_cost = battery_charges * cost_per_charge
    remaining_money = battery_charging_budget - total_charging_cost
    result = remaining_money
    return result

print(solution())