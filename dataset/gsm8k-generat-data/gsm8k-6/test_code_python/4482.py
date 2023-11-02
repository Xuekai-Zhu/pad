def solution():
    # Calculate the number of fruit trees to be planted
    num_fruit_trees = 18 // 2  # every other tree is a fruit tree

    # Calculate the number of each kind of fruit tree to be planted
    num_each_tree = num_fruit_trees // 3  # they want equal numbers of each kind of fruit tree

    result = (num_each_tree, num_each_tree, num_each_tree)  # return tuple of number of plum, pear, and apricot trees
    return result

print(solution())