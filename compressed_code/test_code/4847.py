def solution():
    
    total_minutes = 24 * 60  
    tv_time = total_minutes / 5
    remaining_time = total_minutes - tv_time
    study_time = remaining_time / 4
    result = study_time
    return result

print(solution())