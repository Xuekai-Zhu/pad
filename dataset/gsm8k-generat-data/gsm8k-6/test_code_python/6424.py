def solution():
    # Calculate the number of students who received an A
    A_students = 0.25 * 32  

    # Calculate the number of students who did not receive an A
    non_A_students = 32 - A_students  

    # Calculate the number of students who got a B or C
    B_or_C_students = (1/4) * non_A_students  

    # Calculate the number of students who failed
    failed_students = non_A_students - B_or_C_students  

    result = failed_students
    return result

print(solution())