def solution():
    """Pauline is buying school supplies. The total amount of all the items she wants to buy add up to $150 before sales tax. Sales tax is 8% of the total amount purchased. How much will Pauline spend on all the items, including sales tax?"""
    total_cost = 150
    sales_tax_percent = 8
    sales_tax_amount = total_cost * (sales_tax_percent / 100)
    total_cost_with_tax = total_cost + sales_tax_amount
    result = total_cost_with_tax
    return result

print(solution())