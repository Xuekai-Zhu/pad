def solution():
    original_price = 1200  # The original price of the perfume is $1200
    increased_price = original_price * 1.1  # The price is increased by 10%
    decreased_price = increased_price * 0.85  # The price is decreased by 15%

    # Calculate the amount by which the final price is lower than the original price
    price_difference = original_price - decreased_price
    result = price_difference
    return result

print(solution())