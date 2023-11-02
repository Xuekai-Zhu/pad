def solution():
    initial_tree_height = 16
    initial_boy_height = 24
    boy_growth_rate = 1
    tree_growth_rate = 2

    # Calculate the height difference between the boy and the tree at the start
    height_difference = initial_tree_height - initial_boy_height

    # Calculate how much the boy will grow until he is 36 inches tall
    boy_growth = (36 - initial_boy_height) * boy_growth_rate

    # Calculate how much the tree will grow in the same amount of time
    tree_growth = boy_growth * tree_growth_rate

    # Calculate the final height of the tree by adding the initial height and the growth
    final_tree_height = initial_tree_height + height_difference + tree_growth
    result = final_tree_height
    return result

print(solution())