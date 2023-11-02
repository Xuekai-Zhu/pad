def solution():
    """Hawkeye is driving to his aunt. He has to charge his battery for $3.5 per charge. If he charged his battery four times, and his battery charging budget was $20, how much money was he left with when he reached his aunt's place?"""
    charge_cost = 3.5
    num_charges = 4
    charging_budget = 20
    total_charge_cost = charge_cost * num_charges
    money_left = charging_budget - total_charge_cost
    result = money_left
    return result

print(solution())