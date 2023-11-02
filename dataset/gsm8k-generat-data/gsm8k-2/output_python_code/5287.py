def solution():
    """Grandma wants to order 5 personalized backpacks for each of her grandchildren's first days of school. The backpacks are 20% off of $20.00 and having their names monogrammed on the back pack will cost $12.00 each. How much will the backpacks cost?"""
    price_per_backpack = 20 * 0.8 + 12
    total_cost = price_per_backpack * 5
    result = total_cost
    return result

print(solution())