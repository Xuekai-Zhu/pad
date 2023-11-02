def solution():
    total_students = 180
    students_bombing = total_students / 4
    students_not_showing = (total_students - students_bombing) / 3
    students_failing = 20
    students_passing = total_students - (students_bombing + students_not_showing + students_failing)
    result = students_passing
    return result

print(solution())