def solution():
    total_seeds_planted = 23
    non_growing_seeds = 5

    # Calculate the number of seeds that grew into plants
    growing_seeds = total_seeds_planted - non_growing_seeds

    # Calculate the number of plants that were not eaten by squirrels and rabbits
    uneaten_plants = growing_seeds // 3

    # Calculate the number of plants that were strangled by weeds
    strangled_plants = uneaten_plants // 3

    # Calculate the total number of plants remaining after weeding and keeping one plant
    total_plants = uneaten_plants - strangled_plants - 2 + 1
    result = total_plants
    return result

print(solution())