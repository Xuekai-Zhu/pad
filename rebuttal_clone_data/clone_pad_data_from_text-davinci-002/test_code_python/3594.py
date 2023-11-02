def solution():
    sale_price = 450
    discount_percentage = 10
    original_price = sale_price / (1 - (discount_percentage / 100))
    original_price = round(original_price, 2)
    result = original_price
    return result

print(solution())