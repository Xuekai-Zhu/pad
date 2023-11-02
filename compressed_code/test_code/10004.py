def solution():
    
    math_second_semester = 80
    art_second_semester = 90
    science_second_semester = 90
    
    math_first_semester = math_second_semester + 10
    art_first_semester = art_second_semester - 15
    science_first_semester = (2/3)*science_second_semester
    
    total_marks = math_first_semester + math_second_semester + art_first_semester + art_second_semester + science_first_semester + science_second_semester
    result = total_marks
    
    return result

print(solution())