def solution():
    """Sonja makes her own peanut butter with peanuts and oil in a blender. She uses a ratio of two ounces of oil to smooth out every eight ounces of peanuts. Her last batch of peanut butter weighed 20 ounces. How many ounces of oil did she use?"""
    peanut_weight = 8
    oil_ratio = 2 / peanut_weight
    total_weight = 20
    peanut_portion = peanut_weight / total_weight
    oil_portion = oil_ratio * peanut_portion
    oil_weight = oil_portion * total_weight
    result = oil_weight
    return result

print(solution())