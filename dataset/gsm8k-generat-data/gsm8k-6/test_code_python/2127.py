def solution():
    # Calculate the final price of the smartphone at Store A and Store B
    price_A = 125 * 0.92  # 8% discount, so 92% of the original price
    price_B = 130 * 0.9  # 10% discount, so 90% of the original price

    # Calculate the price difference between the two stores' smartphones
    price_difference = price_B - price_A
    result = price_difference
    return result

print(solution())