def solution():
    # Calculate the number of coconut trees Randy has
    coconut_trees = (1/2) * 60 - 5  # half as many coconut trees as mango trees, minus 5
    total_trees = 60 + coconut_trees  # total number of trees on Randy's farm
    result = total_trees
    return result

print(solution())