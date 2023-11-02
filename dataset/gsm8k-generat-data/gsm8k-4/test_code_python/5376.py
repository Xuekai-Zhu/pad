def solution():
    """Eva learns for two semesters in a year. In 2019, she scored ten more marks in maths in the first semester than the second, 15 marks less in arts, and 1/3 marks less in science in the first semester than the second. If she got 80 marks in maths in the second semester, 90 marks in arts, and 90 in science, what's the total number of her marks in all the semesters?"""
    # Define the marks of the second semester
    math_marks_second = 80
    arts_marks_second = 90
    science_marks_second = 90

    # Calculate the marks of the first semester
    math_marks_first = math_marks_second + 10
    arts_marks_first = arts_marks_second - 15
    science_marks_first = science_marks_second * 2 / 3

    # Calculate the total marks of both semesters
    total_marks = (math_marks_first + math_marks_second) + (arts_marks_first + arts_marks_second) + (science_marks_first + science_marks_second)

    # return the result
    result = total_marks
    return result

print(solution())