def solution():
    """Madeline has 5 boxes with 24 crayons in each. She noticed that 5/8 of the crayons in the 2 boxes were not yet used. In the 2 other boxes, only 2/3 of the crayons were used while the last box was not entirely used. How many unused crayons did Madeline have?"""
    total_crayons = 5 * 24
    unused_crayons = ((24 * 5/8) * 2) + ((24 * 2/3) * 2) + (24 * (1 - 2/3))
    used_crayons = total_crayons - unused_crayons
    result = unused_crayons
    return result

print(solution())