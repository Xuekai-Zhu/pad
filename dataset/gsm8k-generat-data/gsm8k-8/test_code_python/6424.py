def solution():
    # Calculate the number of students who received an A
    a_students = 0.25 * 32

    # Calculate the number of remaining students
    remaining_students = 32 - a_students

    # Calculate the number of students who received a B or C
    b_c_students = 0.25 * remaining_students

    # Calculate the number of students who failed
    failed_students = remaining_students - b_c_students

    result = failed_students
    return result

print(solution())