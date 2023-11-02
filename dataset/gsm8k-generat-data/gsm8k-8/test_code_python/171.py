def solution():
    # Define the number of plants per tree
    plants_per_tree = 20

    # Calculate the total number of seeds collected
    seeds_collected = 2 * plants_per_tree

    # Calculate the number of seeds planted
    seeds_planted = 0.6 * seeds_collected

    # Calculate the number of trees planted
    trees_planted = seeds_planted / plants_per_tree
    result = trees_planted
    return result

print(solution())