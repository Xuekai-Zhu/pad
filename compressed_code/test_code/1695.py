def solution():
    
    original_price = 120
    discount_price = 0.5 * original_price
    sales_tax = 0.05 * discount_price
    total_cost = discount_price + sales_tax
    result = total_cost
    return result

print(solution())