def solution():
    
    current_total_age = 9 * 8
    current_total_students = 9
    new_student_age = 28
    new_total_age = current_total_age + new_student_age
    new_total_students = current_total_students + 1
    new_average_age = new_total_age / new_total_students
    increase = new_average_age - 8
    result = increase
    return result

print(solution())