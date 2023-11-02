def solution():
    """Carla has 6 sunflowers and 8 dandelions. The sunflowers have 9 seeds per plant and the dandelions have 12 seeds per plant. What percentage of Carla's seeds come from the dandelions?"""
    # Define the number of sunflowers and dandelions
    sunflowers = 6
    dandelions = 8

    # Calculate the number of seeds from each type of plant
    sunflower_seeds = sunflowers * 9
    dandelion_seeds = dandelions * 12

    # Calculate the total number of seeds
    total_seeds = sunflower_seeds + dandelion_seeds

    # Calculate the percentage of seeds from the dandelions
    dandelion_percentage = (dandelion_seeds / total_seeds) * 100

    # return the result
    result = dandelion_percentage
    return result

print(solution())