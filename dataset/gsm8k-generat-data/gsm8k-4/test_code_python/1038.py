def solution():
    """Marge planted 23 seeds in her garden. Five of the seeds never grew into plants. A third of the remaining seeds grew, but the plants were eaten by squirrels and rabbits. A third of the number of uneaten plants were strangled by weeds. Marge pulled two weeds, but liked the flowers on one weed and let the plant grow as part of her garden. How many plants did Marge end up with?"""
    # Define the initial number of seeds and the number of seeds that never grew
    initial_seeds = 23
    no_growth_seeds = 5

    # Calculate the number of remaining seeds
    remaining_seeds = initial_seeds - no_growth_seeds

    # Calculate the number of seeds that grew but were eaten by animals
    eaten_seeds = remaining_seeds // 3

    # Calculate the number of uneaten plants
    uneaten_plants = remaining_seeds - eaten_seeds

    # Calculate the number of plants strangled by weeds and the number of remaining plants
    strangled_plants = uneaten_plants // 3
    remaining_plants = uneaten_plants - strangled_plants

    # Calculate the number of plants after pulling weeds
    remaining_plants -= 1

    # Calculate the final number of plants
    final_plants = remaining_plants + 1

    result = final_plants
    return result

print(solution())