def solution():
    # Calculate the number of students moving to the new school
    num_students_moving = 0.4 * 1590  

    # Calculate the number of students remaining at Harrison Elementary School
    num_students_remaining = 1590 - num_students_moving  

    # Calculate the total number of normal classes needed for each grade level
    normal_classes_per_grade = (num_students_remaining / 3 - 20) / 6  

    # Calculate the number of students in each normal class at the new school
    students_per_normal_class = (num_students_moving + num_students_remaining * 2/3) / (3 * normal_classes_per_grade + 3 * 20)  

    result = int(students_per_normal_class)
    return result

print(solution())