def solution():
    """Harrison Elementary School is overcrowded with 1590 students, so 40% of the students are going to move to a new school. There are 3 grade levels, and each grade level needs one 20-person advanced class and the rest of the students divided evenly into 6 additional classes. How many students will there be in each normal class at the new school? """
    # Calculate the number of students who will move to the new school
    students_to_move = 0.4 * 1590

    # Calculate the number of students remaining in Harrison Elementary School
    remaining_students = 1590 - students_to_move

    # Calculate the number of students in each grade level
    grade_level_students = remaining_students / 3

    # Calculate the number of students in each normal class
    normal_class_students = (grade_level_students - 20) / 6

    # Display the number of students in each normal class
    result = normal_class_students
    return result

print(solution())