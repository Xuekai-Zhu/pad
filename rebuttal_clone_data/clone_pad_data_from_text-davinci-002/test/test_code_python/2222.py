def solution():
    tree_one_height = 50
    tree_one_branches = 200
    tree_two_height = 40
    tree_two_branches = 180
    tree_three_height = 60
    tree_three_branches = 180
    tree_four_height = 34
    tree_four_branches = 153
    total_branches = tree_one_branches + tree_two_branches + tree_three_branches + tree_four_branches
    total_height = tree_one_height + tree_two_height + tree_three_height + tree_four_height
    average_branches_per_foot = total_branches / total_height
    result = average_branches_per_foot
    return result

print(solution())