def solution():
    sale_price = 7500
    discount = 25
    original_price = sale_price / (1 - (discount / 100))
    result = original_price
    return result

print(solution())