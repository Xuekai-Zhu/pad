def solution():
    # Calculate the total cost of the meals
    total_meal_cost = 40 + 15 + 25  # Smoky salmon + black burger + chicken katsu

    # Calculate the 10% service charge
    service_charge = 0.1 * total_meal_cost

    # Calculate the 5% tip
    tip = 0.05 * total_meal_cost

    # Calculate the total bill
    total_bill = total_meal_cost + service_charge + tip

    # Calculate the change from $100
    change = 100 - total_bill
    result = change
    return result

print(solution())