def solution():
    old_wattage = 800
    new_wattage = old_wattage * 1.5
    old_price = 0.12
    new_price = old_price * 1.25
    num_hours = 50

    # Calculate the total kilowatt-hours used by the old computer
    old_kwh_used = old_wattage * num_hours / 1000

    # Calculate the total cost of running the old computer
    old_cost = old_kwh_used * old_price

    # Calculate the total kilowatt-hours used by the new computer
    new_kwh_used = new_wattage * num_hours / 1000

    # Calculate the total cost of running the new computer
    new_cost = new_kwh_used * new_price

    # Calculate the difference in cost between the old and new computers
    cost_difference = new_cost - old_cost
    result = cost_difference
    return result

print(solution())