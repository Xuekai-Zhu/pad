def solution():
    math_homework = 60
    geography_homework = math_homework / 2
    science_homework = (math_homework + geography_homework) / 2

    total_study_time = math_homework + geography_homework + science_homework
    result = total_study_time
    return result

print(solution())