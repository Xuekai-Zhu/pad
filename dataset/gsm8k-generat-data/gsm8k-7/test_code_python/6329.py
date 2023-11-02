def solution():
    num_groups = 3
    group_size = 8
    num_students = num_groups * group_size
    num_left_early = 2
    num_remaining = num_students - num_left_early
    result = num_remaining
    return result

print(solution())