def solution():
    
    trees_per_sharpening = 13
    cost_per_sharpening = 5
    total_cost = 35
    num_sharpenings = total_cost / cost_per_sharpening
    min_trees_chopped = trees_per_sharpening * num_sharpenings
    result = min_trees_chopped
    return result

print(solution())