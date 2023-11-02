def solution():
    original_price = 120
    discount = 0.2 # 20% discount
    new_price = original_price * (1 - discount)
    result = new_price
    return result

# We don't need to consider the height of the lamp in this case, as it doesn't affect the price.

print(solution())