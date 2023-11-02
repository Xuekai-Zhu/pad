def solution():
    # Calculate the new amount of used space after deleting the folder and adding new files
    new_used_space = 12.6 - 4.6 + 2

    # Calculate the amount of free space remaining on the old external drive
    old_free_space = 2.4

    # Calculate the net amount of space that needs to be transferred to the new external drive
    net_space_to_transfer = new_used_space - old_free_space

    # Calculate the amount of free space on the new external drive after the transfer
    new_free_space = 20 - net_space_to_transfer
    result = new_free_space
    return result

print(solution())