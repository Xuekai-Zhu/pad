def solution():
    tree_height = 200
    tree_growth = 50
    weeks_in_a_month = 4
    tree_height_in_4_months = tree_height + (weeks_in_a_month * tree_growth)
    result = tree_height_in_4_months
    return result

print(solution())