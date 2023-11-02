def solution():
    """Grandma wants to order 5 personalized backpacks for each of her grandchildren's first days of school. The backpacks are 20% off of $20.00 and having their names monogrammed on the back pack will cost $12.00 each. How much will the backpacks cost?"""
    backpack_cost = 20 * 0.8  # Applying 20% discount
    monogram_cost = 12
    total_cost = (backpack_cost + monogram_cost) * 5  # Multiplying by number of backpacks (5)
    result = total_cost
    return result

print(solution())