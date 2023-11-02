def solution():
    """A mother planted a 16-inch tree on her son's first birthday. On the day the tree was planted, the boy was 24 inches tall. If the tree grows twice as fast as the boy does, how tall will the tree be by the time the boy is 36 inches tall?"""
    initial_tree_height = 16
    initial_boy_height = 24
    final_boy_height = 36
    tree_growth_rate = 2

    boy_growth_rate = final_boy_height - initial_boy_height
    tree_growth = boy_growth_rate * tree_growth_rate
    final_tree_height = initial_tree_height + tree_growth

    result = final_tree_height
    return result

print(solution())