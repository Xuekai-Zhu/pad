def solution():
    original_price = 120
    discount = 0.5
    reduced_price = original_price * discount
    sales_tax_rate = 0.05
    sales_tax = reduced_price * sales_tax_rate
    total_cost = reduced_price + sales_tax
    result = total_cost
    return result

print(solution())