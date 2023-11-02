def solution():
    num_groups = 10
    sticks_per_group = 15
    total_sticks = 170

    # Calculate the total number of sticks used by all groups
    used_sticks = num_groups * sticks_per_group

    # Calculate the number of sticks left
    sticks_left = total_sticks - used_sticks
    result = sticks_left
    return result

print(solution())