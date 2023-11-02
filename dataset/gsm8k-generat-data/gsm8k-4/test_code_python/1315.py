def solution():
    """Marcus can fit 5 pies in his oven at once. He bakes 7 batches of pies, then slips and drops 8 of them. How many pies are left?"""
    # Calculate the total number of pies baked
    total_pies = 5 * 7

    # Subtract the number of dropped pies
    remaining_pies = total_pies - 8

    result = remaining_pies
    return result

print(solution())