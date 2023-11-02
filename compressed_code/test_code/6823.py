def solution():
    
    total_cost = 150
    sales_tax_percent = 8
    sales_tax_amount = total_cost * (sales_tax_percent / 100)
    total_cost_with_tax = total_cost + sales_tax_amount
    result = total_cost_with_tax
    return result

print(solution())