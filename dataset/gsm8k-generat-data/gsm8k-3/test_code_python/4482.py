def solution():
    """A neighborhood association decided to plant a tree on every street. There are eighteen streets in the neighborhood. The association wanted every other tree to be a fruit tree, and they agreed to plant equal numbers of plum, pear, and apricot trees. How many of each kind of tree will they plant?"""
    # Define the number of streets and trees to be planted
    num_streets = 18
    num_trees = num_streets * 2

    # Define the ratio of fruit trees to non-fruit trees
    fruit_ratio = 1 / 2

    # Calculate the number of fruit trees and non-fruit trees
    num_fruit_trees = round(num_trees * fruit_ratio)
    num_non_fruit_trees = num_trees - num_fruit_trees

    # Calculate the number of each type of fruit tree
    num_plum_trees = round(num_fruit_trees / 3)
    num_pear_trees = num_plum_trees
    num_apricot_trees = num_fruit_trees - (num_plum_trees * 2)

    # Display the number of each type of tree
    result = (num_plum_trees, num_pear_trees, num_apricot_trees)
    return result

print(solution())