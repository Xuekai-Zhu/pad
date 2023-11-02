def solution():
    children = 9 + 12
    group_size = 3
    remainder = children % group_size
    if remainder == 0:
        num_of_groups = children // group_size
    else:
        num_of_groups = (children // group_size) + 1
    result = num_of_groups
    return result

print(solution())