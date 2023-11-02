def solution():
    num_trees = 2
    num_plants_per_tree = 20
    seeds_per_plant = 1
    percent_planted = 0.6

    # Calculate the total number of seeds collected from both trees
    total_seeds = num_trees * num_plants_per_tree * seeds_per_plant

    # Calculate the number of seeds that James plants
    num_seeds_planted = total_seeds * percent_planted

    # Calculate the number of plants that James planted
    num_plants_planted = num_seeds_planted / seeds_per_plant

    # Calculate the number of trees that James planted
    num_trees_planted = num_plants_planted / num_plants_per_tree
    result = num_trees_planted
    return result

print(solution())