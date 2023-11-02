def solution():
    students_gsh = 30
    students_bh = students_gsh * 2
    students_mh = (students_gsh + students_bh) * 3/5
    total_students = students_gsh + students_bh + students_mh
    result = total_students
    return result

print(solution())