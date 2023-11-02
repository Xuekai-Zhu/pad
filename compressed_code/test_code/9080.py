def solution():
    
    free_space = 2.4
    used_space = 12.6
    deleted_folder = 4.6
    new_files = 2
    updated_used_space = used_space - deleted_folder + new_files
    new_drive_size = 20
    new_free_space = new_drive_size - updated_used_space
    result = new_free_space
    return result

print(solution())