def solution():
    marks_maths_first = 80
    marks_maths_second = 80 + 10
    marks_arts_first = 90
    marks_arts_second = 90 - 15
    marks_science_first = 90
    marks_science_second = 90 - (90/3)
    total_marks = marks_maths_first + marks_maths_second + marks_arts_first + marks_arts_second + marks_science_first + marks_science_second
    result = total_marks
    return result

print(solution())