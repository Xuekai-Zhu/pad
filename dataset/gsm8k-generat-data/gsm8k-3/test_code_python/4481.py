def solution():
    """Four tires and one battery together cost $224. Each tire costs $42. Calculate the price of the battery."""
    # Define the cost of each tire and the total cost of four tires
    TIRE_PRICE = 42
    FOUR_TIRES_PRICE = 4 * TIRE_PRICE

    # Calculate the price of the battery
    battery_price = 224 - FOUR_TIRES_PRICE

    # Display the price of the battery
    result = battery_price
    return result

print(solution())