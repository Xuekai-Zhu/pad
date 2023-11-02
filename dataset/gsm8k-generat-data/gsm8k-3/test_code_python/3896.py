def solution():
    """Edith is a receptionist at a local office and is organizing files into cabinets. She had 60 files and finished organizing half of them this morning. She has another 15 files to organize in the afternoon and the rest of the files are missing. How many files are missing?"""
    # Define the initial number of files
    initial_files = 60

    # Calculate the number of files organized in the morning
    morning_files = initial_files // 2

    # Calculate the number of files left to organize
    afternoon_files = 15
    remaining_files = initial_files - morning_files - afternoon_files

    # Display the number of missing files
    result = remaining_files
    return result

print(solution())