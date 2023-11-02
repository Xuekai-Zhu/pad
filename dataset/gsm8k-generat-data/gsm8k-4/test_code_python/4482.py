def solution():
    """A neighborhood association decided to plant a tree on every street. There are eighteen streets in the neighborhood.
    The association wanted every other tree to be a fruit tree, and they agreed to plant equal numbers of plum, pear, and apricot trees.
    How many of each kind of tree will they plant?"""
    # Define the number of streets and calculate the total number of trees that need to be planted
    num_streets = 18
    total_trees = num_streets * 2

    # Calculate the number of fruit trees that need to be planted
    fruit_trees = total_trees // 2

    # Divide the fruit trees evenly between the three types of fruit trees
    num_of_each = fruit_trees // 3

    # Calculate the number of plum, pear, and apricot trees
    num_plum = num_of_each
    num_pear = num_of_each
    num_apricot = num_of_each

    # If there are leftover trees, add them to the plum trees
    leftover = fruit_trees % 3
    num_plum += leftover

    # Return the number of each kind of tree
    result = (num_plum, num_pear, num_apricot)
    return result

print(solution())