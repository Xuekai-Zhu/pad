def solution():
    
    tree_one_growth = 1
    tree_two_growth = tree_one_growth * 2
    tree_three_growth = 2
    tree_four_growth = tree_three_growth + 1
    total_growth = (tree_one_growth + tree_two_growth + tree_three_growth + tree_four_growth) * 4
    result = total_growth
    return result

print(solution())