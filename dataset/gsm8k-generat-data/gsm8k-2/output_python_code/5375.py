def solution():
    """Eva learns for two semesters in a year. In 2019, she scored ten more marks in maths in the first semester than the second,
    15 marks less in arts, and 1/3 marks less in science in the first semester than the second. If she got 80 marks in maths in the
    second semester, 90 marks in arts, and 90 in science, what's the total number of her marks in all the semesters?"""
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