def solution():
    # Calculate growth rates for each tree
    tree1_rate = 1
    tree2_rate = 2 * tree1_rate
    tree3_rate = 2
    tree4_rate = tree3_rate + 1

    # Calculate total growth for each tree over 4 days
    tree1_growth = tree1_rate * 4
    tree2_growth = tree2_rate * 2
    tree3_growth = tree3_rate * 4
    tree4_growth = tree4_rate * 4

    # Calculate total growth for all trees
    total_growth = tree1_growth + tree2_growth + tree3_growth + tree4_growth
    result = total_growth
    return result

print(solution())