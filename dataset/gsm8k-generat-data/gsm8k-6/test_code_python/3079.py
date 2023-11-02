def solution():
    # Calculate the cost of a pair of jeans after the summer discount
    jean_price_after_discount = 14.50 * 0.5  # 50% discount applied
    # Calculate the cost of a pair of jeans after the Wednesday discount
    jean_price_final = jean_price_after_discount - 10  # additional $10.00 off on Wednesdays
    # Calculate the original cost of a pair of jeans before all discounts
    original_jean_price = jean_price_final / 0.5
    result = original_jean_price
    return result

print(solution())