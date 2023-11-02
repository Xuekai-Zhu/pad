def solution():
    # Calculate the number of trees that fell
    total_fallen = 5
    narra_fallen = (total_fallen - 1) // 2
    mahogany_fallen = total_fallen - narra_fallen

    # Calculate the number of newly planted trees
    narra_planted = 2 * narra_fallen
    mahogany_planted = 3 * mahogany_fallen

    # Calculate the total number of trees in the farm
    total_trees = 50 + 30 - total_fallen + narra_planted + mahogany_planted
    result = total_trees
    return result

print(solution())