def solution():
    """Harrison Elementary School is overcrowded with 1590 students, so 40% of the students are going to move to a new school. There are 3 grade levels, and each grade level needs one 20-person advanced class and the rest of the students divided evenly into 6 additional classes. How many students will there be in each normal class at the new school?"""
    # Define the initial number of students
    initial_students = 1590

    # Calculate the number of students moving to the new school
    moving_students = initial_students * 0.4

    # Calculate the number of students remaining at Harrison Elementary School
    remaining_students = initial_students - moving_students

    # Calculate the number of students per grade level
    grade_level_students = remaining_students / 3

    # Calculate the number of students in each normal class
    normal_class_students = (grade_level_students - 20) / 6

    # return the result
    result = normal_class_students
    return result

print(solution())