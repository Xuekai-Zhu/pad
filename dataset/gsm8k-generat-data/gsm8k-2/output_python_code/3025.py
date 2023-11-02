def solution():
    """Carla has 6 sunflowers and 8 dandelions. The sunflowers have 9 seeds per plant and the dandelions have 12 seeds per plant. What percentage of Carla's seeds come from the dandelions?"""
    sunflower_seeds = 6 * 9
    dandelion_seeds = 8 * 12
    total_seeds = sunflower_seeds + dandelion_seeds
    dandelion_percentage = (dandelion_seeds / total_seeds) * 100
    result = dandelion_percentage
    return result

print(solution())