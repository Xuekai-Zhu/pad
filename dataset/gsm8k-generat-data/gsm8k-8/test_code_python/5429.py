def solution():
    total_sticks = 170
    num_groups = 10
    sticks_per_group = 15
    
    sticks_given = num_groups * sticks_per_group
    sticks_left = total_sticks - sticks_given
    result = sticks_left
    
    return result

print(solution())