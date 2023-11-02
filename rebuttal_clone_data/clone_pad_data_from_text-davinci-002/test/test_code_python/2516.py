def solution():
    iPhones_purchased = 3
    iPhone_price = 600
    discount_rate = 5
    discount_multiplier = 1 - (discount_rate / 100)
    total_price = iPhones_purchased * iPhone_price
    discounted_price = total_price * discount_multiplier
    savings = total_price - discounted_price
    result = savings
    return result

print(solution())