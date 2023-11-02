def solution():
    # Cost of four tires
    tire_cost = 4 * 42

    # Total cost of four tires and one battery
    total_cost = 224

    # Cost of one battery
    battery_cost = total_cost - tire_cost
    result = battery_cost
    return result

print(solution())