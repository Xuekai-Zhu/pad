def solution():
    apple_count = 180
    fruit_picked = 3/5

    # Calculate the number of apples picked by Damien
    apples_picked = apple_count * fruit_picked

    # Calculate the number of apples remaining on the tree
    apples_remaining = apple_count - apples_picked

    # Calculate the number of plums on the plum tree
    plums_count = apples_count/3

    # Calculate the number of plums picked by Damien
    plums_picked = plums_count * fruit_picked

    # Calculate the number of plums remaining on the tree
    plums_remaining = plums_count - plums_picked

    # Calculate the total number of fruits remaining on both trees
    total_fruits_remaining = apples_remaining + plums_remaining
    result = total_fruits_remaining
    return result

print(solution())