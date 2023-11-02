def solution():
    reduced_price = 6  # The price of the shirt after it has been reduced
    original_price_percentage = 25  # The percentage by which the price has been reduced

    # Calculate the original price of the shirt
    original_price = reduced_price * 100 / (100 - original_price_percentage)
    result = original_price
    return result

print(solution())