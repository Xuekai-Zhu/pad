def solution():
    # Calculate the number of seeds produced by the first plant
    first_plant_seeds = 50

    # Calculate the number of seeds that landed on good soil and will germinate
    germinated_seeds = first_plant_seeds / 2

    # Calculate the number of seedling plants that will grow
    seedling_plants = germinated_seeds

    # Calculate the total number of seeds produced by the seedling plants in two months
    total_seed_output = seedling_plants * 50 * 2

    result = total_seed_output
    return result

print(solution())