def solution():
    max_price = 1000
    discount = 0.2  # 20% discount
    tv_price = (max_price + 100) * (1 - discount)
    difference = max_price - tv_price
    result = difference
    return result

print(solution())