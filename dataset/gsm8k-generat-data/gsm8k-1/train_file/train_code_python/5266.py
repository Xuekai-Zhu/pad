def solution():
    """James bought a gallon of milk for $3, a bunch of bananas for $2, and paid 20% sales tax. How much money did James spend?"""
    milk_cost = 3
    banana_cost = 2
    total_cost = milk_cost + banana_cost
    sales_tax_percent = 20
    sales_tax = total_cost * (sales_tax_percent / 100)
    total_cost_with_tax = total_cost + sales_tax
    result = total_cost_with_tax
    return result

print(solution())