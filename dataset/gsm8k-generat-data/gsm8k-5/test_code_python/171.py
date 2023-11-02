def solution():
    plants_per_tree = 20  # Each tree has 20 plants
    seeds_per_plant = 1  # Each plant has 1 seed
    seedlings_planted_percentage = 60  # James plants 60% of the collected seeds

    # Calculate the total number of seeds collected from both trees
    total_seeds_collected = plants_per_tree * seeds_per_plant * 2

    # Calculate the number of seedlings planted
    seedlings_planted = total_seeds_collected * (seedlings_planted_percentage / 100)

    # Calculate the number of trees planted
    trees_planted = seedlings_planted / plants_per_tree
    result = trees_planted
    return result

print(solution())