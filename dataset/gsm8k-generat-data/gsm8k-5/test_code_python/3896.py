def solution():
    initial_files = 60  # Edith had 60 files
    morning_organized = initial_files / 2  # Edith organized half in the morning
    afternoon_organized = 15  # Edith organized 15 files in the afternoon
    total_organized = morning_organized + afternoon_organized  # Total files organized

    # Calculate the number of missing files
    missing_files = initial_files - total_organized
    result = missing_files
    return result

print(solution())