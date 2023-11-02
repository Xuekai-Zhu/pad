def solution():
    # Calculate how much the boy will grow from 24 to 36 inches tall
    boy_growth = 36 - 24

    # Calculate how much the tree will grow in the same time period
    tree_growth = 2 * boy_growth

    # Add the initial height of the tree to the growth to find the final height
    final_height = 16 + tree_growth
    result = final_height
    return result

print(solution())