def solution():
    """Brennan was researching his school project and had to download files from the internet to his computer to use for reference. After downloading 800 files, he deleted 70% of them because they were not helpful. He downloaded 400 more files but again realized that 3/5 of them were irrelevant. How many valuable files was he left with after deleting the unrelated files he downloaded in the second round?"""
    # Define the initial number of files and the percentage to be deleted
    initial_files = 800
    first_delete_percentage = 0.7

    # Calculate the number of files after the first deletion
    first_round_files = initial_files * (1 - first_delete_percentage)

    # Define the number of files downloaded in the second round and the percentage to be deleted
    second_round_files = 400
    second_delete_fraction = 3/5

    # Calculate the number of files after the second deletion
    final_files = first_round_files + second_round_files - (second_round_files * second_delete_fraction)

    # return the result
    result = final_files
    return result

print(solution())