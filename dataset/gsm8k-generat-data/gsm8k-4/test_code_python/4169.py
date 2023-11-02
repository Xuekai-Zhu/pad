def solution():
    """An apple tree has three times as many apples as the number of plums on a plum tree. If Damien picks 3/5 of the fruits from the trees, calculate the total number of plums and apples remaining on the tree if there were 180 apples on the apple tree before Damien picked any of the fruits."""
    # Define the ratio of apples to plums
    ratio = 3

    # Calculate the number of plums on the plum tree
    plums = 180 / (ratio + 1)

    # Calculate the number of apples on the apple tree
    apples = ratio * plums

    # Calculate the total number of fruits before Damien picked any
    total_fruits = apples + plums

    # Calculate the number of fruits picked by Damien
    picked_fruits = total_fruits * 3/5

    # Calculate the number of fruits remaining on the trees
    remaining_fruits = total_fruits - picked_fruits

    # Calculate the number of plums and apples remaining
    remaining_plums = plums - (picked_fruits / 4)
    remaining_apples = apples - (picked_fruits * 3/4)

    # Return the result
    result = (remaining_plums, remaining_apples)
    return result

print(solution())