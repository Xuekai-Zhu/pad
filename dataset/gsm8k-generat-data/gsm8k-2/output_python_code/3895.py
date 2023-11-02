def solution():
    """Edith is a receptionist at a local office and is organizing files into cabinets. She had 60 files and finished organizing half of them this morning. She has another 15 files to organize in the afternoon and the rest of the files are missing. How many files are missing?"""
    finished_in_morning = 60 / 2
    remaining_to_finish = 15
    total_files = finished_in_morning + remaining_to_finish + missing_files
    missing_files = total_files - 60
    result = missing_files
    return result

print(solution())