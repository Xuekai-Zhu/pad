def solution():
    # Calculate the number of trees Amiyah cut down
    trees_cut_down = 400 * 0.2

    # Calculate the number of trees she planted for each one she cut down
    new_trees_planted = 5

    # Calculate the total number of new trees planted
    total_new_trees = trees_cut_down * new_trees_planted

    # Calculate the total number of trees on the farm after cutting and planting
    total_trees = 400 - trees_cut_down + total_new_trees
    result = total_trees
    return result

print(solution())