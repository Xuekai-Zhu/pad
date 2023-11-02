def solution():
    """Gargamel needed new tires for his truck. He went to the auto shop and bought 4 tires on sale for $75 each. The salesman told him that he saved a total of $36. If Gargamel saved the same amount on each tire, what was the original price of each tire?"""
    total_saved = 36
    number_of_tires = 4
    sale_price = 75
    total_sale_price = sale_price * number_of_tires
    original_price_per_tire = (total_sale_price + total_saved) / number_of_tires
    result = original_price_per_tire
    return result

print(solution())