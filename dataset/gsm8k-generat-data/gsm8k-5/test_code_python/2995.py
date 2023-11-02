def solution():
    total_trees = 400  # There are 400 trees on the farm
    trees_cut = 0.2 * total_trees  # Amiyah cuts 20% of the trees
    trees_planted = 5 * trees_cut  # Amiyah plants 5 new trees for every tree she cuts

    # Calculate the new total number of trees on the farm
    total_trees = total_trees - trees_cut + trees_planted
    result = total_trees
    return result

print(solution())