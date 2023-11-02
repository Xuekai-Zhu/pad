def solution():
    """Robert is building a 15 foot long, 10 foot wide, rectangular wooden fence around his garden. He needs 2 wood slats for every foot of fencing he builds. How many wooden slats will he need?"""
    length = 15
    width = 10
    perimeter = 2 * (length + width)
    slats_per_foot = 2
    total_slats = perimeter * slats_per_foot
    result = total_slats
    return result

print(solution())