def solution():
    # Define the total number of files
    total_files = 60

    # Calculate the number of files organized this morning
    morning_files = total_files / 2

    # Calculate the number of files left to organize
    remaining_files = 15

    # Calculate the number of missing files
    missing_files = total_files - morning_files - remaining_files
    result = missing_files
    return result

print(solution())