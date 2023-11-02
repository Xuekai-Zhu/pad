def solution():
    total_trees = 400 #initial total number of trees
    cut_trees = 0.2 * total_trees #20% of the trees cut
    planted_trees = 5 * cut_trees #5 new trees planted for every cut tree
    remaining_trees = total_trees - cut_trees + planted_trees #total remaining trees after cutting and planting
    result = remaining_trees
    return result

print(solution())