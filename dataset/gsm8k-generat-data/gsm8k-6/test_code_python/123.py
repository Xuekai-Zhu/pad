def solution():
    # Calculate the price per can at the bulk warehouse
    price_bulk = 12 / 48  # $12.00 for 48 cans

    # Calculate the price per can at the local grocery store
    price_grocery = 6 / 12  # $6.00 for 12 cans

    # Calculate the price difference per can between the two options in cents
    price_difference = (price_grocery - price_bulk) * 100

    result = price_difference
    return result

print(solution())