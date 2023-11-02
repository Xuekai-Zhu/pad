def solution():
    
    sticks_per_group = 15
    num_groups = 10
    total_sticks = sticks_per_group * num_groups
    sticks_left = 170 - total_sticks
    result = sticks_left
    return result

print(solution())