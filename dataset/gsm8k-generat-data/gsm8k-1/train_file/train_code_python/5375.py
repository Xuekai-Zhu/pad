def solution():
    """Eva learns for two semesters in a year. In 2019, she scored ten more marks in maths in the first semester than the second, 15 marks less in arts, and 1/3 marks less in science in the first semester than the second. If she got 80 marks in maths in the second semester, 90 marks in arts, and 90 in science, what's the total number of her marks in all the semesters?"""
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