def solution():
    mahogany_trees = 50
    narra_trees = 30
    total_trees = mahogany_trees + narra_trees

    # Calculate the number of trees that fell
    trees_fell = 5
    narra_fell = (trees_fell - 1) / 2  # One more Mahogany tree fell than the number of Narra trees that fell
    mahogany_fell = narra_fell + 1

    # Calculate the number of new trees planted a month after the typhoon
    narra_planted = 2 * narra_fell
    mahogany_planted = 3 * mahogany_fell

    # Calculate the total number of trees on the farm after the typhoon and planting
    total_trees = total_trees - trees_fell + narra_planted + mahogany_planted
    result = total_trees
    return result

print(solution())