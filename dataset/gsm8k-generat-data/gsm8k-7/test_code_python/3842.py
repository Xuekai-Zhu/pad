def solution():
    total_cost = 340
    shirt_price_ratio = 0.75
    shoe_price_diff = 10

    # Let x be the price of the pants
    x = (total_cost - shoe_price_diff) / (1 + shirt_price_ratio + shirt_price_ratio)

    # Calculate the price of the shirt
    shirt_price = shirt_price_ratio * x

    # Calculate the price of the shoes
    shoe_price = x + shoe_price_diff

    result = x
    return result

print(solution())