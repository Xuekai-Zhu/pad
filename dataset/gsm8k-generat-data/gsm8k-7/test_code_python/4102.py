def solution():
    num_units = 18
    paid_price = 500
    discount = 0.2  # 20% discount
    original_price = paid_price / ((num_units > 15) * (1 - discount) + (num_units <= 15))
    result = original_price
    return result

print(solution())