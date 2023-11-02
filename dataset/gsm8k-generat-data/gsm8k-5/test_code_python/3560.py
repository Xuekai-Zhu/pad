def solution():
    salads_needed = 12  # Anna wants to have at least 12 large salads
    lettuce_per_salad = 1/3  # Each large salad needs 1/3 of a lettuce plant
    lettuce_lost = 0.5  # Half of the lettuce will be lost to insects and rabbits

    # Calculate the total lettuce needed, including losses
    total_lettuce_needed = salads_needed / lettuce_per_salad / (1 - lettuce_lost)

    # Round up to the nearest whole number of lettuce plants
    lettuce_plants_needed = math.ceil(total_lettuce_needed)
    result = lettuce_plants_needed
    return result

print(solution())