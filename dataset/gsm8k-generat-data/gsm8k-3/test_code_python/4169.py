def solution():
    """An apple tree has three times as many apples as the number of plums on a plum tree. If Damien picks 3/5 of the fruits from the trees, calculate the total number of plums and apples remaining on the tree if there were 180 apples on the apple tree before Damien picked any of the fruits."""
    # Calculate the number of plums on the plum tree
    apples_on_tree = 180
    plums_on_tree = apples_on_tree / 3

    # Calculate the number of fruits picked by Damien
    fruits_picked = 3/5 * (apples_on_tree + plums_on_tree)

    # Calculate the number of fruits remaining on the trees
    remaining_fruits = apples_on_tree + plums_on_tree - fruits_picked

    # Calculate the number of remaining apples and plums
    remaining_apples = remaining_fruits / 4 * 3
    remaining_plums = remaining_fruits / 4

    # Display the number of remaining fruits
    result = remaining_apples + remaining_plums
    return result

print(solution())