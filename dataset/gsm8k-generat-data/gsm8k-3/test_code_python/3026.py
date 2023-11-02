def solution():
    """Carla has 6 sunflowers and 8 dandelions. The sunflowers have 9 seeds per plant and the dandelions have 12 seeds per plant. What percentage of Carla's seeds come from the dandelions?"""
    # Calculate the total number of seeds from the sunflowers
    sunflower_seeds = 6 * 9

    # Calculate the total number of seeds from the dandelions
    dandelion_seeds = 8 * 12

    # Calculate the total number of seeds
    total_seeds = sunflower_seeds + dandelion_seeds

    # Calculate the percentage of seeds from the dandelions
    dandelion_percent = (dandelion_seeds / total_seeds) * 100

    # Display the percentage of seeds from the dandelions
    result = dandelion_percent
    return result

print(solution())