def solution():
    # Calculate the price per ounce of the larger box
    price_per_ounce_large = 4.80 / 30

    # Calculate the price per ounce of the smaller box
    price_per_ounce_small = 3.40 / 20

    # Find the lowest price per ounce
    if price_per_ounce_large < price_per_ounce_small:
        result = round(price_per_ounce_large * 100)
    else:
        result = round(price_per_ounce_small * 100)
    return result

print(solution())