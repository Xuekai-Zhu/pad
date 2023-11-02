def solution():
    """James collects all the fruits from his 2 trees. Each tree has 20 plants. Each plant has 1 seed and he plants 60% of those. How many trees did he plant?"""
    # Define the number of trees and plants per tree
    num_trees = 2
    plants_per_tree = 20

    # Calculate the total number of plants
    total_plants = num_trees * plants_per_tree

    # Calculate the number of seeds collected
    seeds_collected = total_plants * 1

    # Calculate the number of seeds planted
    seeds_planted = seeds_collected * 0.6

    # Calculate the number of trees planted
    trees_planted = seeds_planted / plants_per_tree

    # Return the result
    result = round(trees_planted)
    return result

print(solution())