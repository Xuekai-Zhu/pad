def solution():
    original_price = 200
    sale_price = original_price * 0.75  # 25% off means paying 75% of the original price
    price_with_tax = sale_price * 1.1  # 10% sales tax means paying 110% of the sale price
    result = price_with_tax
    return result

print(solution())