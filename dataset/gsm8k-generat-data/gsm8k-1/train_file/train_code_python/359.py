def solution():
    """Sonja makes her own peanut butter with peanuts and oil in a blender. She uses a ratio of two ounces of oil to smooth out every eight ounces of peanuts. Her last batch of peanut butter weighed 20 ounces. How many ounces of oil did she use?"""
    peanut_weight = 8
    oil_weight = 2
    ratio = oil_weight / peanut_weight
    peanut_butter_weight = 20
    oil_used = (peanut_butter_weight / peanut_weight) * oil_weight
    result = oil_used
    return result

print(solution())