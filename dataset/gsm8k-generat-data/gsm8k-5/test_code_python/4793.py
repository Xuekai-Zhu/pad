def solution():
    # Calculate the growth of each tree in 4 days
    growth_tree1 = 1 * 4
    growth_tree2 = (1 * 2) * 4
    growth_tree3 = 2 * 4
    growth_tree4 = (2 + 1) * 4

    # Calculate the total growth of all trees in 4 days
    total_growth = growth_tree1 + growth_tree2 + growth_tree3 + growth_tree4
    result = total_growth
    return result

print(solution())