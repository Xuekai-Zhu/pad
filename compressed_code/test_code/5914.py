def solution():
    
    num_trees = 2
    num_plants_per_tree = 20
    num_seeds_per_plant = 1
    percent_seeds_planted = 60
    num_seeds_planted = (num_trees * num_plants_per_tree * num_seeds_per_plant * percent_seeds_planted) / 100
    num_trees_planted = num_seeds_planted / num_seeds_per_plant
    result = num_trees_planted
    return result

print(solution())