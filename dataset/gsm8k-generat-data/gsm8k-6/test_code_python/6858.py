def solution():
    original_price = 1200  # original price of the luxury perfume
    increased_price = original_price + (0.1 * original_price)  # increased price after a 10% increase
    decreased_price = increased_price - (0.15 * increased_price)  # decreased price after a 15% decrease
    price_difference = original_price - decreased_price  # calculate the difference between the original and final price

    result = price_difference
    return result

print(solution())