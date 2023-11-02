def solution():
    initial_tree_height = 16  # The tree was 16 inches tall when it was planted
    initial_boy_height = 24  # The boy was 24 inches tall on the day the tree was planted
    boy_growth = 36 - initial_boy_height  # The boy needs to grow 36 - 24 = 12 inches more
    tree_growth = boy_growth * 2  # The tree grows twice as fast as the boy does

    # Calculate the final height of the tree when the boy is 36 inches tall
    final_tree_height = initial_tree_height + tree_growth
    result = final_tree_height
    return result

print(solution())