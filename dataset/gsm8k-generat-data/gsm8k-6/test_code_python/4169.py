def solution():
    # Calculate the number of apples on the tree after Damien picks some fruits
    remaining_apples = 0.4 * 180  # Damien picks 3/5 of the fruits, so 2/5 remain
    # Calculate the number of plums on the tree
    plums = remaining_apples / 3  # the apple tree has three times as many apples as plums
    # Calculate the total number of fruits remaining on both trees
    total_fruits = remaining_apples + plums
    result = total_fruits
    return result

print(solution())