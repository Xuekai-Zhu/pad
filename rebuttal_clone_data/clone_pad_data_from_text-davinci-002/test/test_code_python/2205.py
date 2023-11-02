def solution():
    total_files = 60
    files_organized = total_files / 2
    files_remaining = total_files - files_organized
    files_missing = files_remaining - 15
    result = files_missing
    return result

print(solution())