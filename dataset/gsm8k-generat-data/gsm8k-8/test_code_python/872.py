def solution():
    original_price = 20
    sale_percent = 15
    sale_price = original_price * (100 - sale_percent) / 100
    pins = 10
    total_price = pins * sale_price
    result = total_price
    return result

print(solution())