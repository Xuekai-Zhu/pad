def solution():
    """Alan has 8 pine trees in his backyard and each tree drops 200 pine cones. If 30% of the pine cones fall on Alan's roof, and each pine cone weighs 4 ounces, how many ounces of pine cones does Alan have on his roof?"""
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