def solution():
    
    students_in_restroom = 2
    students_absent = 3 * students_in_restroom - 1
    desks_full = 4 * 6 * 2 / 3
    total_students = desks_full + students_in_restroom + students_absent
    result = total_students
    return result

print(solution())