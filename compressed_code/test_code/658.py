def solution():
    
    original_price = 20
    discount_percentage = 0.15
    sale_price = original_price - (original_price * discount_percentage)
    quantity = 10
    total_cost = sale_price * quantity
    result = total_cost
    return result

print(solution())