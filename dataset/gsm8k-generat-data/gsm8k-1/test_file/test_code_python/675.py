def solution():
    """If 6 potatoes makes 36 hash browns, how many hash browns can you make out of 96 potatoes?"""
    potatoes_per_hashbrown = 6
    total_potatoes = 96
    total_hashbrowns = (total_potatoes/potatoes_per_hashbrown)*36
    result = total_hashbrowns
    return result

print(solution())