def solution():
    original_price = 24 * 7  # price of 24 tickets without discount
    discount = 0.5  # 50% discount
    discounted_price = original_price * (1 - discount)  # price after discount
    result = discounted_price
    return result

print(solution())