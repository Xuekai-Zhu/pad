def solution():
    """Calculate the price of the house that Jill and Bob bought."""
    # Define the total price of both houses
    total_price = 600000

    # Define the price of the first house, which they bought
    house1_price = total_price / 3

    # Define the price of the second house
    house2_price = house1_price * 2

    # Return the price of the first house
    result = house1_price
    return result

print(solution())