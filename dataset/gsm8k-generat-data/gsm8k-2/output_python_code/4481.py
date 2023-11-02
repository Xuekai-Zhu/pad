def solution():
    """A neighborhood association decided to plant a tree on every street. There are eighteen streets in the neighborhood. The association wanted every other tree to be a fruit tree, and they agreed to plant equal numbers of plum, pear, and apricot trees. How many of each kind of tree will they plant?"""
    total_trees = 18
    fruit_trees = total_trees // 2
    each_fruit_tree = fruit_trees // 3
    plum_trees = each_fruit_tree
    pear_trees = each_fruit_tree
    apricot_trees = each_fruit_tree
    result = (plum_trees, pear_trees, apricot_trees)
    return result

print(solution())