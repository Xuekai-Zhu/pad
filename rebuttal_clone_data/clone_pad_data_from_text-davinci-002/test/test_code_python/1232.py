def solution():
    num_students = 10
    num_affected_students = 9
    current_average_age = 8
    new_student_age = 28
    total_age = num_affected_students * current_average_age + new_student_age
    new_average_age = total_age / num_students
    age_difference = new_average_age - current_average_age
    result = age_difference
    return result

print(solution())