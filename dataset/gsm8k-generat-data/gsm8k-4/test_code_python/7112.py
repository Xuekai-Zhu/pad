def solution():
    """Asia bought a homecoming dress on sale for $140. It was originally priced at $350. What percentage off did she get at the sale?"""
    # Define the original and sale prices
    original_price = 350
    sale_price = 140

    # Calculate the difference in price
    price_diff = original_price - sale_price

    # Calculate the percentage off
    percentage_off = (price_diff / original_price) * 100

    # return the result
    result = percentage_off
    return result

print(solution())