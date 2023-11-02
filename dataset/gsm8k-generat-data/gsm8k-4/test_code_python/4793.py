def solution():
    """There are four growing trees. The first tree grows 1 meter/day, the second grows the same amount in half the time, the third grows 2 meters/day, and the fourth tree grows a meter more than the third each day. How many meters did the trees grow in total in 4 days?"""
    # Define the growth rates of each tree
    tree1_rate = 1
    tree2_rate = 2 * tree1_rate
    tree3_rate = 2
    tree4_rate = tree3_rate + 1

    # Calculate the total growth of each tree in 4 days
    tree1_growth = tree1_rate * 4
    tree2_growth = tree2_rate * 4
    tree3_growth = tree3_rate * 4
    tree4_growth = tree4_rate * 4

    # Calculate the total growth of all trees
    total_growth = tree1_growth + tree2_growth + tree3_growth + tree4_growth

    result = total_growth
    return result

print(solution())