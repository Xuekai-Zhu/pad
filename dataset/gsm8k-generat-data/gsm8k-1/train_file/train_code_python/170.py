def solution():
    """James collects all the fruits from his 2 trees. Each tree has 20 plants. Each plant has 1 seed and he plants 60% of those. How many trees did he plant?"""
    num_trees = 2
    num_plants_per_tree = 20
    num_seeds_per_plant = 1
    percent_seeds_planted = 60
    num_seeds_planted = (num_trees * num_plants_per_tree * num_seeds_per_plant * percent_seeds_planted) / 100
    num_trees_planted = num_seeds_planted / num_seeds_per_plant
    result = num_trees_planted
    return result

print(solution())