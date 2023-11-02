def solution():
    """There are 32 students in a statistics course. 25 percent of the class received an A. 1/4 of the remaining students got either a B or C, and the rest of the students failed. How many students failed?"""
    # Define the total number of students
    total_students = 32

    # Calculate the number of students who received an A
    A_students = total_students * 0.25

    # Calculate the number of remaining students
    remaining_students = total_students - A_students

    # Calculate the number of students who received a B or C
    BC_students = remaining_students / 4

    # Calculate the number of students who failed
    failed_students = total_students - A_students - BC_students

    result = failed_students
    return result

print(solution())