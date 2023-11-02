def solution():
    """Marlene wants to buy half a dozen of shirts to avail of the sale. The regular price of a shirt is $50 and is now on sale at a 20% discount. How much will Marlene pay for the shirts?"""
    num_shirts = 6
    price_per_shirt = 50
    discount_percentage = 0.2
    sale_price_per_shirt = price_per_shirt - (price_per_shirt * discount_percentage)
    total_price = num_shirts * sale_price_per_shirt
    result = total_price
    return result

print(solution())