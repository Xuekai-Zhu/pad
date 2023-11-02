def solution():
    """Sonja makes her own peanut butter with peanuts and oil in a blender. She uses a ratio of two ounces of oil to smooth out every eight ounces of peanuts. Her last batch of peanut butter weighed 20 ounces. How many ounces of oil did she use?"""
    # Define the ratio of oil to peanuts
    OIL_PER_PEANUTS = 2/8

    # Define the weight of peanuts in the batch
    peanuts_weight = 20/(OIL_PER_PEANUTS + 1)

    # Calculate the weight of oil in the batch
    oil_weight = peanuts_weight * OIL_PER_PEANUTS

    # Display the weight of oil used
    result = oil_weight
    return result

print(solution())