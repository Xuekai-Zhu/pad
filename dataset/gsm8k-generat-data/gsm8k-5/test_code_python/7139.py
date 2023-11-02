def solution():
    num_books = 400
    target_group_size = 24

    # Keep dividing the groups in half until the target group size is reached
    num_divisions = 0
    while num_books > target_group_size:
        num_books /= 2
        num_divisions += 1

    result = num_divisions
    return result

print(solution())