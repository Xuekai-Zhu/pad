def solution():
    """Sarah's external drive showed 2.4 gigabytes free and 12.6 gigabytes used. She decided to delete a folder of size 4.6 gigabytes and store new files of 2 gigabytes. If she will transfer all her files to a new external drive of size 20 gigabytes, how many free gigabytes will the new external drive have?"""
    # Define the initial free and used space on the external drive
    initial_free_space = 2.4
    initial_used_space = 12.6

    # Calculate the new free and used space after deleting a folder and storing new files
    new_used_space = initial_used_space - 4.6 + 2
    new_free_space = 20 - new_used_space

    # Display the new free space on the new external drive
    result = new_free_space
    return result

print(solution())