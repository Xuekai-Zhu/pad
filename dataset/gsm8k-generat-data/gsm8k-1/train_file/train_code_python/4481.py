def solution():
    """A neighborhood association decided to plant a tree on every street. There are eighteen streets in the neighborhood. The association wanted every other tree to be a fruit tree, and they agreed to plant equal numbers of plum, pear, and apricot trees. How many of each kind of tree will they plant?"""
    streets = 18
    fruit_trees = streets // 2
    trees_per_fruit = 3
    total_trees = fruit_trees * trees_per_fruit
    trees_per_type = total_trees // 3
    plums = trees_per_type
    pears = trees_per_type
    apricots = trees_per_type
    result = (plums, pears, apricots)
    return result

print(solution())