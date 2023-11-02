def solution():
    external_drive_size = 20
    used_space = 12.6
    deleted_space = 4.6
    added_space = 2
    total_used_space = used_space - deleted_space + added_space
    free_space = external_drive_size - total_used_space
    result = free_space
    return result

print(solution())