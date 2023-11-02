def solution():
    original_price = 120
    discount_percent = 50
    sales_tax_percent = 5
    discount_amount = original_price * (discount_percent / 100)
    reduced_price = original_price - discount_amount
    sales_tax_amount = reduced_price * (sales_tax_percent / 100)
    total_cost = reduced_price + sales_tax_amount
    result = total_cost
    return result

print(solution())