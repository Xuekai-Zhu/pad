def solution():
    # Calculate the number of lemon trees in the grove
    num_trees = 50 * 30

    # Calculate the total number of lemons produced in a year by one tree
    normal_lemons_per_tree = 60
    engineered_lemons_per_tree = normal_lemons_per_tree * 1.5

    # Calculate the total number of lemons produced in a year by all the trees
    normal_lemons_per_year = num_trees * normal_lemons_per_tree
    engineered_lemons_per_year = num_trees * engineered_lemons_per_tree

    # Calculate the total number of lemons produced in 5 years
    total_normal_lemons = normal_lemons_per_year * 5
    total_engineered_lemons = engineered_lemons_per_year * 5

    result = total_engineered_lemons
    return result

print(solution())