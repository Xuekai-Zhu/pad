def solution():
    # define the growth rates
    tree1_growth_rate = 1
    tree2_growth_rate = 2
    tree3_growth_rate = 4
    tree4_growth_rate = 5

    # total growth over 4 days
    tree1_growth = tree1_growth_rate * 4
    tree2_growth = tree2_growth_rate * 4
    tree3_growth = tree3_growth_rate * 4
    tree4_growth = tree4_growth_rate * 4

    # total growth
    total_growth = tree1_growth + tree2_growth + tree3_growth + tree4_growth

    # return the result
    return total_growth

print(solution())