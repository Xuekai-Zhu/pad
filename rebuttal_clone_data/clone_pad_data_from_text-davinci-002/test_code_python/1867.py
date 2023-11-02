def solution():
    total_students = 20
    students_in_classroom = total_students / 4
    students_on_playground = total_students - students_in_classroom
    boys_on_playground = students_on_playground / 3
    girls_on_playground = students_on_playground - boys_on_playground
    result = girls_on_playground
    return result

print(solution())