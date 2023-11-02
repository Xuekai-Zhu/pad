def solution():
    """There are 50 children at the party. Three-fifths of them are boys. How many of the children are girls?"""
    total_children = 50
    boys_fraction = 3/5
    boys_count = total_children * boys_fraction
    girls_count = total_children - boys_count
    result = girls_count
    return result

print(solution())