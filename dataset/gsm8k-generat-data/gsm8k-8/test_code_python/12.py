def solution():
    # Define the number of mango trees
    mango_trees = 60

    # Calculate the number of coconut trees
    coconut_trees = (mango_trees / 2) - 5

    # Calculate the total number of trees
    total_trees = mango_trees + coconut_trees
    result = total_trees
    return result

print(solution())