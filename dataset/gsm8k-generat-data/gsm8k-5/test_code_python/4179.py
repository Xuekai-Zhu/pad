def solution():
    # Calculate the new used space on the external drive
    new_used_space = 12.6 - 4.6 + 2  # 4.6 GB folder deleted, and 2 GB of new files added

    # Calculate the free space on the new external drive
    new_free_space = 20 - new_used_space

    result = new_free_space
    return result

print(solution())