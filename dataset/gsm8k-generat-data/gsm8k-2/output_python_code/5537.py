def solution():
    """The ratio of cows to bulls in a barn is 10:27. If there are 555 cattle on the farm, how many bulls are on the farm?"""
    total_cattle = 555
    cow_ratio = 10
    bull_ratio = 27
    total_ratio = cow_ratio + bull_ratio
    bull_count = (bull_ratio / total_ratio) * total_cattle
    result = bull_count
    return result

print(solution())