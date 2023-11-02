def solution():
    """Carla is taking attendance for her sixth-grade class. She knows that 2 students are in the restroom, and one less than three times that number of students are absent. If there are four rows with six desks each that are all 2/3 full, how many students does Carla teach, including the ones in and out of the classroom?"""
    # Calculate the number of students absent
    students_in_restroom = 2
    absent_students = 3 * students_in_restroom - 1

    # Calculate the number of students in the classroom
    desks_full = 6 * 4 * (2/3)  # Total number of full desks
    students_in_classroom = int(desks_full)  # Round down to the nearest integer

    # Calculate the total number of students
    total_students = students_in_classroom + students_in_restroom + absent_students

    # Return the result
    result = total_students
    return result

print(solution())