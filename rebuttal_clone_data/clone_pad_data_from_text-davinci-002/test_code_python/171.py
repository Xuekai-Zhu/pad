def solution():
     """James collects all the fruits from his 2 trees. Each tree has 20 plants. Each plant has 1 seed and he plants 60% of those. How many trees did he plant?"""
    trees = 2
    plants_per_tree = 20
    seeds_per_plant = 1
    percent_planted = 60
    total_seeds = trees * plants_per_tree * seeds_per_plant
    total_planted = total_seeds * (percent_planted / 100)
    result = total_planted
    
    return result

print(solution())