def solution():
 
    initial_number_of_students = 160
    new_students = 20
    total_students = initial_number_of_students + new_students
    students_who_left = total_students / 3
    final_number_of_students = total_students - students_who_left
    result = final_number_of_students
    return result

print(solution())