def solution():
    good_oranges_A = 10 * 0.6  # number of good oranges from tree A
    good_oranges_B = 15 * (1/3)  # number of good oranges from tree B
    total_good_oranges = 55  # total number of good oranges
    num_trees_A = 0.5 * total_good_oranges / good_oranges_A  # calculate number of tree A
    num_trees_B = 0.5 * total_good_oranges / good_oranges_B  # calculate number of tree B
    total_trees = num_trees_A + num_trees_B  # total number of trees
    result = total_trees
    return result

print(solution())