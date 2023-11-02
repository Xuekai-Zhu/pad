def solution():
    
    total_students = 60
    students_with_6_allowance = total_students * (2/3)
    students_with_4_allowance = total_students - students_with_6_allowance
    allowance_from_6_students = students_with_6_allowance * 6
    allowance_from_4_students = students_with_4_allowance * 4
    total_allowance = allowance_from_6_students + allowance_from_4_students
    result = total_allowance
    return result

print(solution())