def solution():
    
    total_students = 32
    a_students = total_students * 0.25
    remaining_students = total_students - a_students
    b_or_c_students = remaining_students / 4
    failed_students = total_students - a_students - b_or_c_students
    result = failed_students
    return result

print(solution())