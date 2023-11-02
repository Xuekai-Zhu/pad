def solution():
    battery_charge_cost = 3.5
    num_charges = 4
    battery_charge_budget = 20

    # Calculate the total cost of all battery charges
    total_charge_cost = battery_charge_cost * num_charges

    # Calculate the amount of money Hawkeye has left after paying for all battery charges
    amount_left = battery_charge_budget - total_charge_cost
    result = amount_left
    return result

print(solution())