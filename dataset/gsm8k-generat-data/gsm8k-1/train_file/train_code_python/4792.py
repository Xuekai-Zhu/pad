def solution():
    """
    There are four growing trees. The first tree grows 1 meter/day, the second grows the same amount in half the time,
    the third grows 2 meters/day, and the fourth tree grows a meter more than the third each day.
    How many meters did the trees grow in total in 4 days?
    """
    tree_one_growth = 1
    tree_two_growth = tree_one_growth * 2
    tree_three_growth = 2
    tree_four_growth = tree_three_growth + 1
    total_growth = (tree_one_growth + tree_two_growth + tree_three_growth + tree_four_growth) * 4
    result = total_growth
    return result

print(solution())