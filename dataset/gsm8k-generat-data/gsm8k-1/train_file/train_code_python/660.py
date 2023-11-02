def solution():
    """There are 30 different nuts in a bowl. If 5/6 of the nuts were eaten, how many nuts were left?"""
    total_nuts = 30
    eaten_fraction = 5/6
    remaining_fraction = 1 - eaten_fraction
    nuts_left = remaining_fraction * total_nuts
    result = nuts_left
    return result

print(solution())