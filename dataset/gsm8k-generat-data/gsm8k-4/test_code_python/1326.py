def solution():
    """Gargamel needed new tires for his truck. He went to the auto shop and bought 4 tires on sale for $75 each. The salesman told him that he saved a total of $36. If Gargamel saved the same amount on each tire, what was the original price of each tire?"""
    # Define the sale price and the total savings
    sale_price = 75
    total_savings = 36

    # Calculate the original price of each tire
    original_price = (sale_price * 4 + total_savings) / 4

    # Return the result
    result = original_price
    return result

print(solution())