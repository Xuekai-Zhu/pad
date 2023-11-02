def solution():
    
    total_time = 3 * 60  
    math_time = 45
    english_time = 30
    science_time = 50
    history_time = 25
    homework_time = math_time + english_time + science_time + history_time
    special_project_time = total_time - homework_time
    result = special_project_time
    return result

print(solution())