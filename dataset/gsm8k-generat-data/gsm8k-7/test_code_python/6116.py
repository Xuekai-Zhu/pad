def solution():
    num_trees = 8
    num_cones_per_tree = 200
    percent_fall_on_roof = 0.30
    weight_per_cone = 4  # ounces

    # Calculate the total number of pine cones that fall on Alan's roof
    total_cones_on_roof = num_trees * num_cones_per_tree * percent_fall_on_roof

    # Calculate the total weight of the pine cones on Alan's roof
    total_weight_on_roof = total_cones_on_roof * weight_per_cone
    result = total_weight_on_roof
    return result

print(solution())