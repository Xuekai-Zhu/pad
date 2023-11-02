def solution():
    total_cost = 600
    shirt_price_ratio = 1 / 3

    # Let x be the price of the coat in dollars
    # Then the price of the shirt is (1/3)x dollars
    # Total cost is x + (1/3)x = (4/3)x dollars
    # Solving for x: (4/3)x = total_cost
    # x = (3/4)total_cost
    coat_price = (3 / 4) * total_cost

    # The price of the shirt is (1/3) of the coat price
    shirt_price = shirt_price_ratio * coat_price
    result = shirt_price
    return result

print(solution())