def solution():
    # Calculate the rate of growth for the tree and the boy
    tree_growth_rate = 2
    boy_growth_rate = 1

    # Calculate the time it will take for the boy to grow to 36 inches
    boy_growth_time = (36 - 24) / boy_growth_rate

    # Calculate the height of the tree after the boy has grown to 36 inches
    tree_growth_time = boy_growth_time * tree_growth_rate
    tree_height = 16 + (tree_growth_time * 2)

    result = tree_height
    return result

print(solution())