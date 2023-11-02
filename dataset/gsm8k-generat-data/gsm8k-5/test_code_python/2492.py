def solution():
    total_items = 7 + 4  # Vanessa sold a total of 7 dresses and 4 shirts
    total_earnings = 69  # Vanessa made a total of $69 from the sales
    price_per_shirt = 5  # Vanessa sold each shirt for $5

    # Calculate the total earnings from the sale of the dresses
    earnings_from_dresses = total_earnings - (total_items * price_per_shirt)

    # Calculate the price per dress
    price_per_dress = earnings_from_dresses / 7
    result = price_per_dress
    return result

print(solution())