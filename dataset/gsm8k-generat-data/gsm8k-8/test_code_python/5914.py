def solution():
    # Define the variables and unknowns
    total_trees = x
    tree_A = 0.5 * total_trees
    tree_B = 0.5 * total_trees
    oranges_A = 10 * tree_A
    oranges_B = 15 * tree_B
    good_oranges_A = 0.6 * oranges_A
    good_oranges_B = (1/3) * oranges_B
    total_good_oranges = 55

    # Set up and solve the equation for total trees
    equation = good_oranges_A + good_oranges_B - total_good_oranges
    x = equation / ((0.6 * 10) + (1/3 * 15))

    result = round(x)
    return result

print(solution())