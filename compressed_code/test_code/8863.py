def solution():
    
    total_files = 60
    morning_files = total_files / 2
    afternoon_files = 15
    missing_files = total_files - (morning_files + afternoon_files)
    result = missing_files
    return result

print(solution())