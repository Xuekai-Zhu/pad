def solution():
    original_price = 200
    discount_percent = 25
    sales_tax_percent = 10
    discount_amount = original_price * (discount_percent / 100)
    sale_price = original_price - discount_amount
    tax_amount = sale_price * (sales_tax_percent / 100)
    total_price = sale_price + tax_amount
    result = total_price
    
    return result

print(solution())