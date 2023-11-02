def solution():
    
    total_students = 1800
    foreign_students_percentage = 0.3
    current_foreign_students = total_students * foreign_students_percentage
    new_foreign_students = 200
    total_foreign_students = current_foreign_students + new_foreign_students
    result = total_foreign_students
    return result

print(solution())