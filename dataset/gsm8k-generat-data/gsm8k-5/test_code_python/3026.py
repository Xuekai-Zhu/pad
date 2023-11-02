def solution():
    # Calculate the total number of seeds from the sunflowers
    sunflower_seeds = 6 * 9

    # Calculate the total number of seeds from the dandelions
    dandelion_seeds = 8 * 12

    # Calculate the total number of seeds from both plants
    total_seeds = sunflower_seeds + dandelion_seeds

    # Calculate the percentage of seeds that come from the dandelions
    dandelion_percentage = (dandelion_seeds / total_seeds) * 100
    result = dandelion_percentage
    return result

print(solution())