def solution():
    
    tree_1 = 1000
    tree_2 = tree_1 / 2
    tree_3 = tree_2
    tree_4 = tree_1 + 200
    total_height = tree_1 + tree_2 + tree_3 + tree_4
    num_trees = 4
    average_height = total_height / num_trees
    result = average_height
    return result

print(solution())