def solution():
    # Define the cost of one tire
    tire_cost = 42

    # Calculate the total cost of four tires
    four_tires_cost = 4 * tire_cost

    # Calculate the cost of the battery by subtracting the cost of four tires from the total cost
    battery_cost = 224 - four_tires_cost

    result = battery_cost
    return result

print(solution())