def solution():
    # Calculate the price per can at the bulk warehouse
    price_per_can_bulk = 12.00 / 48

    # Calculate the price per can at the grocery store
    price_per_can_grocery = 6.00 / 12

    # Calculate the difference in price per can
    difference = (price_per_can_grocery - price_per_can_bulk) * 100

    result = difference
    return result

print(solution())