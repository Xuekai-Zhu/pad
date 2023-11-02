def solution():
    tree1_growth_rate = 1
    tree2_growth_rate = tree1_growth_rate * 2
    tree3_growth_rate = 2
    tree4_growth_rate = tree3_growth_rate + 1

    num_days = 4

    # Calculate the total growth of each tree in the given number of days
    tree1_growth = tree1_growth_rate * num_days
    tree2_growth = tree2_growth_rate * num_days
    tree3_growth = tree3_growth_rate * num_days
    tree4_growth = tree4_growth_rate * num_days

    # Calculate the total growth of all trees in the given number of days
    total_growth = tree1_growth + tree2_growth + tree3_growth + tree4_growth
    result = total_growth
    return result

print(solution())