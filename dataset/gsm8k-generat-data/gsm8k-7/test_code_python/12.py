def solution():
    num_mango_trees = 60

    # Calculate the number of coconut trees
    num_coconut_trees = (num_mango_trees / 2) - 5

    # Calculate the total number of trees
    total_trees = num_mango_trees + num_coconut_trees
    result = total_trees
    return result

print(solution())