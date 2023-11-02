def solution():
    larger_box_price = 4.80
    larger_box_size = 30

    smaller_box_price = 3.40
    smaller_box_size = 20

    # Calculate the price per ounce for the larger box
    larger_box_price_per_ounce = larger_box_price / larger_box_size

    # Calculate the price per ounce for the smaller box
    smaller_box_price_per_ounce = smaller_box_price / smaller_box_size

    # Determine which box has the better value (lowest price per ounce)
    if larger_box_price_per_ounce < smaller_box_price_per_ounce:
        result = round(larger_box_price_per_ounce * 100)
    else:
        result = round(smaller_box_price_per_ounce * 100)
    return result

print(solution())