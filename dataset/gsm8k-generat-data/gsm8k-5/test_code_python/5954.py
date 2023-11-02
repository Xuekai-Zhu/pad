def solution():
    # Let's call the number of students in Tina/Maura's classroom "x"
    num_students_tm = x

    # Zack's classroom has half the amount of total students between Tina and Maura's classrooms
    total_students = 2*x  # There are 2 classrooms with "x" number of students each
    num_students_z = total_students / 2

    # When Zack was sick there were 22 students in his class
    num_students_z_sick = num_students_z - 1  # Assuming Zack is included in the total count

    # Total number of students between the 3 classrooms
    total_students_all = num_students_tm + num_students_tm + num_students_z
    total_students_all_sick = total_students_all - 1  # Assuming Zack is included in the total count

    # Check if the numbers make sense
    if num_students_z_sick != 22:
        return "Error: Invalid input"

    result = total_students_all_sick
    return result

print(solution())