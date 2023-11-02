def solution():
    # Calculate the number of plums on the plum tree
    apple_to_plum_ratio = 3  # The apple tree has 3 times as many apples as the plum tree
    apples_before = 180  # Damien picked 3/5 of the fruits, so there were 2/5 remaining on the tree
    apples_remaining = apples_before * (3/5)
    plums_remaining = apples_remaining / apple_to_plum_ratio

    # Calculate the total number of remaining fruits
    total_remaining = apples_remaining + plums_remaining
    result = total_remaining
    return result

print(solution())