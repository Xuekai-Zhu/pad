def solution():
    """A mother planted a 16-inch tree on her son's first birthday. On the day the tree was planted, the boy was 24 inches tall. If the tree grows twice as fast as the boy does, how tall will the tree be by the time the boy is 36 inches tall?"""
    # Define the initial height of the tree and the boy
    tree_height = 16
    boy_height = 24

    # Calculate the growth rate of the boy and the tree
    boy_growth_rate = (36 - boy_height) / (12 - 1)
    tree_growth_rate = boy_growth_rate * 2

    # Calculate the height of the tree when the boy is 36 inches tall
    tree_height_at_36 = tree_height + (12 * tree_growth_rate)

    # Return the result
    result = tree_height_at_36
    return result

print(solution())