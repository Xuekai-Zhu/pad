def solution():
    """A mother planted a 16-inch tree on her son's first birthday.  On the day the tree was planted, the boy was 24 inches tall.  If the tree grows twice as fast as the boy does, how tall will the tree be by the time the boy is 36 inches tall?"""
    # Define the initial heights of the tree and the boy
    tree_height = 16
    boy_height = 24

    # Define the growth rates of the tree and the boy
    tree_growth_rate = 2
    boy_growth_rate = 1

    # Calculate the time it takes for the boy to grow to 36 inches tall
    time = (36 - boy_height) / boy_growth_rate

    # Calculate the height of the tree at that time
    tree_height_at_time = tree_height + (time * tree_growth_rate)

    # Display the height of the tree when the boy is 36 inches tall
    result = tree_height_at_time
    return result

print(solution())