def solution():
    # Calculate the number of students who will move to the new school
    move_students = 0.4 * 1590

    # Calculate the total number of students who will remain at Harrison Elementary
    remaining_students = 1590 - move_students

    # Calculate the number of students in each grade level
    grade_level_students = remaining_students / 3

    # Calculate the number of students in each normal class
    normal_class_students = (grade_level_students - 20) / 6

    result = normal_class_students
    return result

print(solution())