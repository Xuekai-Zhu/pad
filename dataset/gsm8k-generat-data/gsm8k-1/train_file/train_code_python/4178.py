def solution():
    """Sarah's external drive showed 2.4 gigabytes free and 12.6 gigabytes used. She decided to delete a folder of size 4.6 gigabytes and store new files of 2 gigabytes. If she will transfer all her files to a new external drive of size 20 gigabytes, how many free gigabytes will the new external drive have?"""
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