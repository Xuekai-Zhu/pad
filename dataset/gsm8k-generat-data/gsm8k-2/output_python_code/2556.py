def solution():
    """If olivine has 5 more precious stones than agate and diamond has 11 more precious stones than olivine, how many precious stones do they have together if agate has 30 precious stones?"""
    agate_precious_stones = 30
    olivine_precious_stones = agate_precious_stones + 5
    diamond_precious_stones = olivine_precious_stones + 11
    total_precious_stones = agate_precious_stones + olivine_precious_stones + diamond_precious_stones
    result = total_precious_stones
    return result

print(solution())