def solution():
    total_books = 400
    target_group_size = 24
    current_group_size = total_books
    num_splits = 0
    
    while current_group_size > target_group_size:
        current_group_size = current_group_size / 2
        num_splits += 1
    
    result = num_splits
    return result

print(solution())