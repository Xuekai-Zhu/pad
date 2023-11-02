def solution():
    total_students = 100
    students_in_grade_4 = 30
    students_in_grade_5 = 35
    students_in_grade_6 = total_students - students_in_grade_4 - students_in_grade_5
    result = students_in_grade_6
    return result

print(solution())