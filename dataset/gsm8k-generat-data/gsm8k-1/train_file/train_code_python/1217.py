def solution():
    """John needs to replace his shoes so he decides to buy a $150 pair of Nikes and a $120 pair of work boots. Tax is 10%. How much did he pay for everything?"""
    nike_price = 150
    boots_price = 120
    tax_rate = 0.1
    subtotal = nike_price + boots_price
    tax = subtotal * tax_rate
    total = subtotal + tax
    result = total
    return result

print(solution())