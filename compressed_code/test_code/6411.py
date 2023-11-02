def solution():
    
    original_price = 200
    discount_percent = 25
    discount_amount = original_price * (discount_percent/100)
    sale_price = original_price - discount_amount
    tax_percent = 10
    tax_amount = sale_price * (tax_percent/100)
    total_cost = sale_price + tax_amount
    result = total_cost
    return result

print(solution())