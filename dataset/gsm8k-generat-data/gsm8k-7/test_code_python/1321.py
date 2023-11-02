def solution():
    total_cost = 150
    sales_tax_rate = 0.08  # 8% sales tax

    # Calculate the sales tax amount
    sales_tax = total_cost * sales_tax_rate

    # Calculate the total cost including sales tax
    total_cost_with_tax = total_cost + sales_tax
    result = total_cost_with_tax
    return result

print(solution())