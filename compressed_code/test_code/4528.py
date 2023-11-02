def solution():
    
    math_homework_time = 60
    geography_homework_time = math_homework_time / 2
    science_homework_time = (math_homework_time + geography_homework_time) / 2
    total_study_time = math_homework_time + geography_homework_time + science_homework_time
    result = total_study_time
    return result

print(solution())