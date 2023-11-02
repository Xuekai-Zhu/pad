def solution():
    # Calculate the price per ounce for both boxes
    price_per_ounce_large = 480 / 30  # price in cents per ounce for the larger box
    price_per_ounce_small = 340 / 20  # price in cents per ounce for the smaller box

    # Determine which box has the better value (lower price per ounce)
    if price_per_ounce_large <= price_per_ounce_small:
        result = price_per_ounce_large
    else:
        result = price_per_ounce_small
    return result

print(solution())