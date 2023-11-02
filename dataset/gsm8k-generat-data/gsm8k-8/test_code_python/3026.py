def solution():
    # Calculate the total number of sunflower seeds
    sunflower_seeds = 6 * 9

    # Calculate the total number of dandelion seeds
    dandelion_seeds = 8 * 12

    # Calculate the total number of seeds
    total_seeds = sunflower_seeds + dandelion_seeds

    # Calculate the percentage of seeds that come from dandelions
    dandelion_percentage = (dandelion_seeds / total_seeds) * 100

    result = dandelion_percentage
    return result

print(solution())