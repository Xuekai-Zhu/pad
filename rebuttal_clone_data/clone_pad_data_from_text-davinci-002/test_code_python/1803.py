def solution():
    total_students = 90
    students_cafeteria = total_students * 2/3
    students_outside = total_students - students_cafeteria
    students_ran_inside = students_outside / 3
    students_in_cafeteria = students_cafeteria + students_ran_inside
    result = students_in_cafeteria
    return result

print(solution())