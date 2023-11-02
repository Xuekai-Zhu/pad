def solution():
    """A small sunflower has 3 dozen seeds and a large sunflower has 50% more seeds than a small sunflower. How many sunflower seeds are there altogether?"""
    small_sunflower_seeds = 3 * 12
    large_sunflower_seeds = small_sunflower_seeds * 1.5
    total_seeds = small_sunflower_seeds + large_sunflower_seeds
    result = total_seeds
    return result

print(solution())