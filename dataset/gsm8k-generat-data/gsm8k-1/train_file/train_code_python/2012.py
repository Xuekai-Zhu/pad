def solution():
    """There are 120 crayons in a box. One third of the crayons are new, 20% are broken, and the rest are slightly used. How many are slightly used?"""
    total_crayons = 120
    new_crayons = total_crayons / 3
    broken_crayons = total_crayons * 0.2
    slightly_used_crayons = total_crayons - new_crayons - broken_crayons
    result = slightly_used_crayons
    return result

print(solution())