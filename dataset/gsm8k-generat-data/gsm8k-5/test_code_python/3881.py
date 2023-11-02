def solution():
    # Calculate the price per ounce for the larger box
    price_per_ounce_larger = 480 / 30  # Convert $4.80 to cents and divide by 30 ounces

    # Calculate the price per ounce for the smaller box
    price_per_ounce_smaller = 340 / 20  # Convert $3.40 to cents and divide by 20 ounces

    # Determine which box has a lower price per ounce
    if price_per_ounce_larger < price_per_ounce_smaller:
        result = price_per_ounce_larger
    else:
        result = price_per_ounce_smaller
    return result

print(solution())