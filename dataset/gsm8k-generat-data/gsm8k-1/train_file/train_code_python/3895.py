def solution():
    """Edith is a receptionist at a local office and is organizing files into cabinets. She had 60 files and finished organizing half of them this morning. She has another 15 files to organize in the afternoon and the rest of the files are missing. How many files are missing?"""
    total_files = 60
    morning_files = total_files / 2
    afternoon_files = 15
    missing_files = total_files - (morning_files + afternoon_files)
    result = missing_files
    return result

print(solution())