def solution():
    students_in_class = 30
    math_students = students_in_class / 5
    english_students = students_in_class / 3
    science_students = (students_in_class - math_students - english_students) / 7
    total_students = math_students + english_students + science_students
    result = students_in_class - total_students
    return result

print(solution())