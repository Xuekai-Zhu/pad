def solution():
    """Martin rings the small bell 4 times more than 1/3 as often as the big bell. If he rings both of them a combined total of 52 times, how many times does he ring the big bell?"""
    total_rings = 52
    small_bell_ratio = 1/3
    small_bell_rings = small_bell_ratio * total_rings
    big_bell_rings = (total_rings - small_bell_rings) / 5
    result = big_bell_rings
    return result

print(solution())