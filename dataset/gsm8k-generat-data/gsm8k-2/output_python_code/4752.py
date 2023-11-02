def solution():
    """Alice is planting bushes around three sides of her yard. If each side is 16 feet long, and each bush fills 4 feet, how many bushes does she need to buy?"""
    side_length = 16
    bush_size = 4
    total_bushes = (3 * side_length) / bush_size
    result = total_bushes
    return result

print(solution())