def solution():
    
    num_shirts = 6
    price_per_shirt = 50
    discount_percentage = 0.2
    sale_price_per_shirt = price_per_shirt - (price_per_shirt * discount_percentage)
    total_price = num_shirts * sale_price_per_shirt
    result = total_price
    return result

print(solution())