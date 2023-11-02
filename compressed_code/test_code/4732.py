def solution():
    
    num_trees = 8
    num_cones_per_tree = 200
    num_cones = num_trees * num_cones_per_tree
    percent_on_roof = 0.3
    num_on_roof = num_cones * percent_on_roof
    weight_per_cone = 4
    total_weight = num_on_roof * weight_per_cone
    result = total_weight
    return result

print(solution())