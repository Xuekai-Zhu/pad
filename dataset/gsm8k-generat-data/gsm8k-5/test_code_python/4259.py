def solution():
    total_sweets = 27  # There are 27 pieces of sweets in the box
    mother_kept = total_sweets / 3  # Mother kept 1/3 of the sweets
    remaining_sweets = total_sweets - mother_kept

    # The eldest child got 8 sweets
    # The youngest child got half as many as the eldest
    # Therefore, the two children got a total of 8 + 4 = 12 sweets
    # The second child gets the remaining sweets
    second_child_sweets = remaining_sweets - 12
    result = second_child_sweets
    return result

print(solution())