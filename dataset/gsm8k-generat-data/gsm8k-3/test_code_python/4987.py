def solution():
    """A bottle of wine costs $20.00 today.  When new tariffs are imposed in 2 months, the price of wine will increase by 25%.  How much more expensive will 5 bottles of wine be in 2 months?"""
    # Define the current price of a bottle of wine
    price_1 = 20.00

    # Calculate the new price of a bottle of wine
    price_2 = price_1 * 1.25

    # Calculate the difference in price per bottle
    price_difference = price_2 - price_1

    # Calculate the total price difference for 5 bottles
    total_difference = price_difference * 5

    # Display the total price difference
    result = total_difference
    return result

print(solution())