def solution():
    """Jeff bought 6 pairs of shoes and 4 jerseys for $560. Jerseys cost 1/4 price of one pair of shoes. Find the shoe's price total price."""
    # Define the number of pairs of shoes and jerseys purchased
    SHOE_PAIRS = 6
    JERSEYS = 4

    # Define the total cost of all the items
    TOTAL_COST = 560

    # Calculate the price of one jersey
    JERSEY_PRICE = 1/4 * (TOTAL_COST - SHOE_PAIRS * x) / JERSEYS

    # Calculate the price of one pair of shoes
    SHOE_PRICE = (TOTAL_COST - JERSEYS * JERSEY_PRICE) / SHOE_PAIRS

    # Calculate the total price of all the pairs of shoes
    SHOE_TOTAL_PRICE = SHOE_PRICE * SHOE_PAIRS

    # Display the total price of all the pairs of shoes
    result = SHOE_TOTAL_PRICE
    return result

print(solution())