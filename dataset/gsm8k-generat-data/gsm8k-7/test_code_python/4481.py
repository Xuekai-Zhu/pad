def solution():
    total_cost = 224
    tire_cost = 42
    num_tires = 4

    # Calculate the total cost of all tires
    total_tire_cost = tire_cost * num_tires

    # Calculate the cost of the battery
    battery_cost = total_cost - total_tire_cost
    result = battery_cost
    return result

print(solution())