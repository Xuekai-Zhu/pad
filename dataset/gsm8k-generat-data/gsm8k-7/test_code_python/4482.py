def solution():
    num_streets = 18
    fruit_tree_percentage = 0.5  # every other tree is a fruit tree
    num_fruit_trees = num_streets / 2
    num_plum_trees = num_fruit_trees / 3
    num_pear_trees = num_fruit_trees / 3
    num_apricot_trees = num_fruit_trees / 3
    result = f"Plum trees: {num_plum_trees}, Pear trees: {num_pear_trees}, Apricot trees: {num_apricot_trees}"
    return result

print(solution())