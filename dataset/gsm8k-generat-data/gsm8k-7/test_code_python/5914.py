def solution():
    num_good_oranges = 55

    # Calculate the number of good oranges from tree A
    num_good_oranges_A = 0.6 * 10 * 0.5

    # Calculate the number of good oranges from tree B
    num_good_oranges_B = (1/3) * 15 * 0.5

    # Calculate the total number of trees
    total_trees = num_good_oranges / (num_good_oranges_A + num_good_oranges_B)
    result = total_trees
    return result

print(solution())