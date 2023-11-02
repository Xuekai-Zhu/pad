def solution():
    initial_free_space = 2.4
    initial_used_space = 12.6
    deleted_folder_size = 4.6
    new_files_size = 2
    new_drive_size = 20

    # Calculate the new used space after deleting the folder and adding new files
    new_used_space = initial_used_space - deleted_folder_size + new_files_size

    # Calculate the free space in the new drive
    new_free_space = new_drive_size - new_used_space
    
    result = new_free_space
    return result

print(solution())