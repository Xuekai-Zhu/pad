def solution():
    streets = 18  # There are 18 streets in the neighborhood
    fruit_trees_per_street = 2  # Every other tree on each street will be a fruit tree
    total_fruit_trees = streets * fruit_trees_per_street  # Calculate the total number of fruit trees needed

    # Calculate the number of each kind of fruit tree needed
    num_each_fruit_tree = total_fruit_trees / 3  # There are three types of fruit trees: plum, pear, and apricot
    num_plum_trees = num_each_fruit_tree
    num_pear_trees = num_each_fruit_tree
    num_apricot_trees = num_each_fruit_tree

    result = (num_plum_trees, num_pear_trees, num_apricot_trees)
    return result

print(solution())