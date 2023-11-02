def solution():
    """Brennan was researching his school project and had to download files from the internet to his computer to use for reference. After downloading 800 files, he deleted 70% of them because they were not helpful. He downloaded 400 more files but again realized that 3/5 of them were irrelevant. How many valuable files was he left with after deleting the unrelated files he downloaded in the second round?"""
    # Define the initial number of files and the percentage of irrelevant files
    files = 800
    irrelevant_percentage = 0.7

    # Calculate the number of relevant files after the first round
    relevant_files = files * (1 - irrelevant_percentage)

    # Define the number of files downloaded in the second round and the percentage of irrelevant files
    new_files = 400
    new_irrelevant_percentage = 0.6

    # Calculate the number of relevant files after the second round
    new_relevant_files = new_files * (1 - new_irrelevant_percentage)

    # Calculate the total number of relevant files
    total_relevant_files = relevant_files + new_relevant_files

    # return the result
    result = total_relevant_files
    return result

print(solution())