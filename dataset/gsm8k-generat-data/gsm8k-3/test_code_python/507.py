def solution():
    """James buys steaks for buy one get one free. The price is $15 per pound and he buys 20 pounds. How much did he pay for the steaks?"""
    # Define the price per pound and the number of pounds bought
    PRICE_PER_POUND = 15
    POUNDS_BOUGHT = 20

    # Calculate the total cost of the steaks
    cost = POUNDS_BOUGHT * PRICE_PER_POUND * 0.5

    # Display the total cost
    result = cost
    return result

print(solution())