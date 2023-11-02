def solution():
    """Carla has 6 sunflowers and 8 dandelions. The sunflowers have 9 seeds per plant and the dandelions have 12 seeds per plant. What percentage of Carla's seeds come from the dandelions?"""
    sunflowers = 6
    dandelions = 8
    sunflower_seeds = sunflowers * 9
    dandelion_seeds = dandelions * 12
    total_seeds = sunflower_seeds + dandelion_seeds
    percentage_dandelion_seeds = (dandelion_seeds / total_seeds) * 100
    result = percentage_dandelion_seeds
    
    return result

print(solution())