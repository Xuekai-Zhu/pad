def solution():
    """John needs to replace his shoes so he decides to buy a $150 pair of Nikes and a $120 pair of work boots. Tax is 10%. How much did he pay for everything?"""
    nikes_price = 150
    work_boots_price = 120
    subtotal = nikes_price + work_boots_price
    tax_rate = 0.1
    total_price = subtotal * (1 + tax_rate)
    result = total_price
    return result

print(solution())