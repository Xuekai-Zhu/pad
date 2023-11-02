def solution():
    # Calculate the number of seeds produced by the original plant
    original_seeds = 50

    # Calculate the number of seedling plants that germinated from the original seeds
    germinated_plants = original_seeds // 2

    # Calculate the total number of seeds produced by the new plants in two months' time
    new_plants_seeds = (germinated_plants * original_seeds) * 2

    result = new_plants_seeds
    return result

print(solution())