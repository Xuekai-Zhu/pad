def solution():
    """Gargamel needed new tires for his truck. He went to the auto shop and bought 4 tires on sale for $75 each. The salesman told him that he saved a total of $36. If Gargamel saved the same amount on each tire, what was the original price of each tire?"""
    # Define the sale price and the amount saved per tire
    SALE_PRICE = 75
    SAVED_AMOUNT_PER_TIRE = 36 / 4

    # Calculate the original price per tire
    original_price = SALE_PRICE + SAVED_AMOUNT_PER_TIRE

    # Display the original price per tire
    result = original_price
    return result

print(solution())