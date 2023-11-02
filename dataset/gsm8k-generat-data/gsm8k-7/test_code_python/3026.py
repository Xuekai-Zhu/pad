def solution():
    num_sunflowers = 6
    sunflower_seeds_per_plant = 9

    num_dandelions = 8
    dandelion_seeds_per_plant = 12

    # Calculate the total number of seeds from the sunflowers
    total_sunflower_seeds = num_sunflowers * sunflower_seeds_per_plant

    # Calculate the total number of seeds from the dandelions
    total_dandelion_seeds = num_dandelions * dandelion_seeds_per_plant

    # Calculate the total number of seeds from both types of plants
    total_seeds = total_sunflower_seeds + total_dandelion_seeds

    # Calculate the percentage of seeds that come from the dandelions
    dandelion_seed_percentage = (total_dandelion_seeds / total_seeds) * 100

    result = dandelion_seed_percentage
    return result

print(solution())