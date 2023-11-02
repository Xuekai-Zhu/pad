def solution():
    # Calculate the prices after discounts
    price_first_store = 950 - (0.06 * 950)  # 6% discount
    price_second_store = 920 - (0.05 * 920)  # 5% discount

    # Calculate the difference in prices
    price_difference = price_first_store - price_second_store
    result = price_difference
    return result

print(solution())