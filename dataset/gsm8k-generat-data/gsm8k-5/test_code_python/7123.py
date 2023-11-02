def solution():
    total_students = 1590  # Total number of students at Harrison Elementary School
    percent_to_move = 0.4  # 40% of the students will move to a new school
    students_to_move = total_students * percent_to_move
    students_remaining = total_students - students_to_move  # Number of students remaining at Harrison Elementary

    # Calculate the number of students in each grade level
    students_per_grade = students_remaining / 3

    # Calculate the number of advanced classes needed per grade
    advanced_classes_per_grade = 3  # Each grade level needs one advanced class

    # Calculate the number of normal classes needed per grade
    normal_classes_per_grade = 6

    # Calculate the number of students in each normal class
    students_per_normal_class = (students_per_grade - advanced_classes_per_grade * 20) / normal_classes_per_grade
    result = students_per_normal_class
    return result

print(solution())