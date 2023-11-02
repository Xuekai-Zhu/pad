def solution():
    
    group_size = 15
    num_groups = 10
    total_sticks_given = group_size * num_groups
    sticks_left = 170 - total_sticks_given
    result = sticks_left
    return result

print(solution())