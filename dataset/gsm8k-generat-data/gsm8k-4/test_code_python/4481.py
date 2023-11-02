def solution():
    """Four tires and one battery together cost $224. Each tire costs $42. Calculate the price of the battery."""
    # Define the cost of one tire and the total cost of four tires
    tire_price = 42
    tires_cost = 4 * tire_price

    # Calculate the cost of the battery
    battery_cost = 224 - tires_cost

    # return the result
    result = battery_cost
    return result

print(solution())