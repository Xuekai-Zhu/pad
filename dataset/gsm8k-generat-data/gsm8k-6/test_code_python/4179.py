def solution():
    # Calculate the total amount of used space after deleting the folder and adding new files
    total_used = 12.6 - 4.6 + 2  # subtract the size of the deleted folder and add the size of the new files

    # Calculate the amount of free space on the old external drive
    free_space = 2.4

    # Calculate the total size of the new external drive
    new_drive_size = 20

    # Calculate the amount of free space on the new external drive
    new_drive_free = new_drive_size - total_used

    result = new_drive_free
    return result

print(solution())