def solution():
    regular_price = 80
    discount_percent = 15
    discount_amount = regular_price * (discount_percent / 100)
    discounted_price = regular_price - discount_amount
    result = discounted_price
    return result

print(solution())