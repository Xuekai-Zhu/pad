def solution():
    """Alice is planting bushes around three sides of her yard. If each side is 16 feet long, and each bush fills 4 feet, how many bushes does she need to buy?"""
    side_length = 16
    bush_width = 4
    bushes_per_side = side_length / bush_width
    total_bushes = int(bushes_per_side * 3)
    result = total_bushes
    return result

print(solution())