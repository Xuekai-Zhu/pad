def solution():
    """Peter needs 80 ounces of soda for his party. He sees that 8 oz cans cost $.5 each. How much does he spend on soda if he buys the exact number of cans he needs?"""
    soda_needed = 80
    can_size = 8
    price_per_can = 0.5
    cans_needed = soda_needed / can_size
    total_cost = cans_needed * price_per_can
    result = total_cost
    return result

print(solution())