def solution():
    """Jeff bought 6 pairs of shoes and 4 jerseys for $560. Jerseys cost 1/4 price of one pair of shoes. Find the shoe's price total price."""
    # Define the number of shoes and jerseys bought
    shoes_bought = 6
    jerseys_bought = 4

    # Define the total cost of the purchase
    total_cost = 560

    # Calculate the cost of one jersey
    jersey_price = 1/4 * (total_cost / (shoes_bought + jerseys_bought))

    # Calculate the cost of one pair of shoes
    shoe_price = total_cost / (2 * shoes_bought + jerseys_bought)

    # Calculate the total cost of the shoes
    shoe_total_price = shoes_bought * shoe_price

    result = shoe_total_price
    return result

print(solution())