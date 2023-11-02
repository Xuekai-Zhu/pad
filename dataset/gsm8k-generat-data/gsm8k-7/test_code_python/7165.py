def solution():
    total_students = 1000
    beach_students = total_students / 2
    remaining_students = total_students - beach_students
    home_students = remaining_students / 2
    students_in_school = remaining_students - home_students
    result = students_in_school
    return result

print(solution())