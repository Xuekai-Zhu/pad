def solution():
    """Big Lots is having a sale. All chairs are 25% off. If you buy more than 5 chairs, you get an additional 1/3 off the discounted price of the number of chairs over 5. If you bought 8 chairs that were normally priced at $20, how much do the chairs cost in total?"""
    # Define the regular price of the chairs
    regular_price = 20

    # Calculate the discounted price of the chairs
    discounted_price = regular_price * 0.75

    # Calculate the price of the first 5 chairs
    first_five_price = discounted_price * 5

    # Calculate the price of the remaining chairs
    remaining_chairs = 8 - 5
    remaining_price = discounted_price * remaining_chairs * (2/3)

    # Calculate the total price of the chairs
    total_price = first_five_price + remaining_price

    # Return the result
    result = total_price
    return result

print(solution())