def solution():
    num_sets = 2
    knives_per_set = 4
    cost_per_set = 80.0

    # Calculate the total number of knives
    total_knives = num_sets * knives_per_set

    # Calculate the cost per knife
    cost_per_knife = cost_per_set / total_knives
    result = cost_per_knife
    return result

print(solution())