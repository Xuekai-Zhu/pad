def solution():
    total_books = 400
    final_group_size = 24

    # Calculate how many times the initial groups need to be divided to reach the final group size
    num_divisions = 0
    current_group_size = total_books
    while current_group_size > final_group_size:
        current_group_size /= 2
        num_divisions += 1

    result = num_divisions
    return result

print(solution())