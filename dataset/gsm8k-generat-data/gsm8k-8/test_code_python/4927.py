def solution():
    first_tree_height = 1000
    second_tree_height = 0.5 * first_tree_height
    third_tree_height = 0.5 * first_tree_height
    fourth_tree_height = first_tree_height + 200

    total_height = first_tree_height + second_tree_height + third_tree_height + fourth_tree_height
    num_trees = 4

    average_height = total_height / num_trees
    result = average_height
    return result

print(solution())