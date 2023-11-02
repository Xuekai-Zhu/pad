def solution():
    """James collects all the fruits from his 2 trees. Each tree has 20 plants. Each plant has 1 seed and he plants 60% of those. How many trees did he plant?"""
    tree_plants = 20
    seeds_per_plant = 1
    planted_seeds_percentage = 0.6
    total_seeds_planted = 2 * tree_plants * seeds_per_plant * planted_seeds_percentage
    trees_planted = total_seeds_planted / tree_plants
    result = trees_planted
    return result

print(solution())