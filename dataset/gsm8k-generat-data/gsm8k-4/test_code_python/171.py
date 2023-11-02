def solution():
    """James collects all the fruits from his 2 trees. Each tree has 20 plants. Each plant has 1 seed and he plants 60% of those. How many trees did he plant?"""
    # Define the number of trees and plants per tree
    num_trees = 2
    plants_per_tree = 20

    # Calculate the total number of seeds
    total_seeds = num_trees * plants_per_tree

    # Calculate the number of seeds planted
    planted_seeds = total_seeds * 0.6

    # Calculate the number of trees planted
    trees_planted = planted_seeds / plants_per_tree

    # Return the result
    result = trees_planted
    return result

print(solution())