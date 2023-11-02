def solution():
    mango_trees = 60  # Randy has 60 mango trees on his farm
    coconut_trees = (1/2) * mango_trees - 5  # Randy has 5 less than half as many coconut trees as mango trees
    total_trees = mango_trees + coconut_trees  # Total number of trees on Randy's farm
    result = total_trees
    return result

print(solution())