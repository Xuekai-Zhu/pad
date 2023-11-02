def solution():
    """Pauline is buying school supplies. The total amount of all the items she wants to buy add up to $150 before sales tax. Sales tax is 8% of the total amount purchased. How much will Pauline spend on all the items, including sales tax?"""
    total_price = 150
    sales_tax_percent = 0.08
    sales_tax = total_price * sales_tax_percent
    total_price_with_tax = total_price + sales_tax
    result = total_price_with_tax
    return result

print(solution())