def solution():
    num_students = 1590
    percent_moving = 0.4
    num_grades = 3
    advanced_class_size = 20
    num_additional_classes = 6

    # Calculate the number of students moving to the new school
    num_moving = int(num_students * percent_moving)

    # Calculate the number of students remaining at Harrison Elementary
    num_remaining = num_students - num_moving

    # Calculate the number of students per grade level
    num_per_grade = num_remaining // num_grades

    # Calculate the number of students in the advanced class at the new school
    num_advanced_class = advanced_class_size * num_grades

    # Calculate the remaining students to be divided evenly into additional classes
    remaining_students = num_per_grade - num_advanced_class

    # Calculate the number of students in each additional class
    num_normal_class = remaining_students // num_additional_classes
    result = num_normal_class
    return result

print(solution())