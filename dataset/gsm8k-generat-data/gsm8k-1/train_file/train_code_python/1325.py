def solution():
    """Gargamel needed new tires for his truck. He went to the auto shop and bought 4 tires on sale for $75 each. The salesman told him that he saved a total of $36. If Gargamel saved the same amount on each tire, what was the original price of each tire?"""
    sale_price = 75
    total_savings = 36
    saved_per_tire = total_savings / 4
    original_price = sale_price + saved_per_tire
    result = original_price
    return result

print(solution())