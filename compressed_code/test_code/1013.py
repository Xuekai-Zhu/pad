def solution():
    
    total_price = 150
    sales_tax_percent = 0.08
    sales_tax = total_price * sales_tax_percent
    total_price_with_tax = total_price + sales_tax
    result = total_price_with_tax
    return result

print(solution())