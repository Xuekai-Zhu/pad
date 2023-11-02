def solution():
    total_pine_cones = 8 * 200  # Alan has 8 pine trees, and each tree drops 200 pine cones
    pine_cones_on_roof = 0.3 * total_pine_cones  # 30% of the pine cones fall on Alan's roof
    weight_per_pine_cone = 4  # Each pine cone weighs 4 ounces

    # Calculate the total weight of pine cones on Alan's roof
    total_weight = pine_cones_on_roof * weight_per_pine_cone
    result = total_weight
    return result

print(solution())