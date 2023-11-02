def solution():
    # Calculate the total growth of each tree in 4 days
    tree_1_growth = 1 * 4  # first tree grows 1 meter/day
    tree_2_growth = 2 * 4  # second tree grows at double the rate of the first tree
    tree_3_growth = 4 * 2  # third tree grows 2 meters/day
    tree_4_growth = (4 * (2 + 1))  # fourth tree grows a meter more than the third each day

    # Calculate the total growth of all trees
    total_growth = tree_1_growth + tree_2_growth + tree_3_growth + tree_4_growth
    result = total_growth
    return result

print(solution())