def solution():
    # Calculate the total number of seeds from sunflowers and dandelions
    sunflower_seeds = 6 * 9  # 6 sunflowers with 9 seeds per plant
    dandelion_seeds = 8 * 12  # 8 dandelions with 12 seeds per plant
    total_seeds = sunflower_seeds + dandelion_seeds

    # Calculate the percentage of seeds that come from dandelions
    dandelion_percentage = (dandelion_seeds / total_seeds) * 100
    result = dandelion_percentage
    return result

print(solution())