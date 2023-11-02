def solution():
    """Sonja makes her own peanut butter with peanuts and oil in a blender. She uses a ratio of two ounces of oil to smooth out every eight ounces of peanuts. Her last batch of peanut butter weighed 20 ounces. How many ounces of oil did she use?"""
    # Define the ratio of oil to peanuts
    oil_to_peanuts_ratio = 2 / 8

    # Calculate the weight of peanuts in the batch
    peanut_weight = 20 / (oil_to_peanuts_ratio + 1)

    # Calculate the weight of oil in the batch
    oil_weight = oil_to_peanuts_ratio * peanut_weight

    # return the result
    result = oil_weight
    return result

print(solution())