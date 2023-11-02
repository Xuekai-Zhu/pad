def solution():
    """Jeff bought 6 pairs of shoes and 4 jerseys for $560. Jerseys cost 1/4 price of one pair of shoes. Find the shoe's price total price."""
    num_shoes = 6
    num_jerseys = 4
    total_cost = 560
    jersey_price_ratio = 1/4
    # Let x be the price of one pair of shoes
    # Then the price of one jersey is x * jersey_price_ratio
    # The total cost can be expressed as 6x + 4(x * jersey_price_ratio) = 560
    # Simplifying the equation gives x = 80, the price of one pair of shoes
    shoe_price = 80
    total_shoe_price = num_shoes * shoe_price
    result = total_shoe_price
    return result

print(solution())