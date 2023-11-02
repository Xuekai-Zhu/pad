def solution():
    """A mother planted a 16-inch tree on her son's first birthday. On the day the tree was planted, the boy was 24 inches tall. If the tree grows twice as fast as the boy does, how tall will the tree be by the time the boy is 36 inches tall?"""
    initial_tree_height = 16
    boy_height_on_planting_day = 24
    boy_growth_rate = 12  # inches per year (as he grew 12 inches from age 1 to 2)
    tree_growth_rate = boy_growth_rate * 2
    boy_height_at_target_tree_height = boy_height_on_planting_day + (initial_tree_height * 0.5)  # boy is half way to tree height
    years_to_reach_target_height = (36 - boy_height_at_target_tree_height) / boy_growth_rate
    tree_height_at_target_boy_height = initial_tree_height + (tree_growth_rate * years_to_reach_target_height)
    result = tree_height_at_target_boy_height
    return result

print(solution())