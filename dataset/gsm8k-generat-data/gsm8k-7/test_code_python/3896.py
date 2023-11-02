def solution():
    total_files = 60
    finished_files = 30
    afternoon_files = 15

    # Calculate the number of missing files
    missing_files = total_files - (finished_files + afternoon_files)
    result = missing_files
    return result

print(solution())