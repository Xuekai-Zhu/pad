def solution():
    """There are 50 children at the party. Three-fifths of them are boys. How many of the children are girls?"""
    total_children = 50
    boys = (3/5) * total_children
    girls = total_children - boys
    result = girls
    return result

print(solution())