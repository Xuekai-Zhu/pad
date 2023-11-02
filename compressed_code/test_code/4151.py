def solution():
    
    math_second_sem = 80
    arts_second_sem = 90
    science_second_sem = 90
    math_first_sem = math_second_sem + 10
    arts_first_sem = arts_second_sem - 15
    science_first_sem = (2/3) * science_second_sem
    total_marks = math_first_sem + math_second_sem + arts_first_sem + arts_second_sem + science_first_sem + science_second_sem
    result = total_marks
    return result

print(solution())