def solution():
    """If olivine has 5 more precious stones than agate and diamond has 11 more precious stones than olivine, how many precious stones do they have together if agate has 30 precious stones?"""
    agate_stones = 30
    olivine_stones = agate_stones + 5
    diamond_stones = olivine_stones + 11
    total_stones = agate_stones + olivine_stones + diamond_stones
    result = total_stones
    return result

print(solution())