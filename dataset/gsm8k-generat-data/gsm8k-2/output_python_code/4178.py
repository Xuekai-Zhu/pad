def solution():
    """Sarah's external drive showed 2.4 gigabytes free and 12.6 gigabytes used. She decided to delete a folder of size 4.6 gigabytes and store new files of 2 gigabytes.
    If she will transfer all her files to a new external drive of size 20 gigabytes, how many free gigabytes will the new external drive have?"""
    
    # Original drive
    original_total = 2.4 + 12.6
    original_free = 2.4
    
    # After deleting folder and adding files
    new_total = original_total - 4.6 + 2
    new_free = original_free - 4.6 + 2
    
    # Free space on new external drive
    new_drive_size = 20
    new_free_drive = new_drive_size - new_total
    
    result = new_free_drive
    return result

print(solution())