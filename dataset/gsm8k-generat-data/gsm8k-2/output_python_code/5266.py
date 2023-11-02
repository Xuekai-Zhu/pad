def solution():
    """James bought a gallon of milk for $3, a bunch of bananas for $2, and paid 20% sales tax. How much money did James spend?"""
    milk_cost = 3
    banana_cost = 2
    total_cost = milk_cost + banana_cost
    sales_tax_percent = 0.2
    sales_tax_amount = total_cost * sales_tax_percent
    total_cost_with_tax = total_cost + sales_tax_amount
    result = total_cost_with_tax
    return result

print(solution())