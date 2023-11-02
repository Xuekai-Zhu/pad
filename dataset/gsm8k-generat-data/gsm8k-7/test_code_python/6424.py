def solution():
    num_students = 32

    # Calculate the number of students who got an A
    num_a_students = round(num_students * 0.25)

    # Calculate the number of remaining students
    num_remaining_students = num_students - num_a_students

    # Calculate the number of students who got a B or C
    num_b_or_c_students = round(num_remaining_students * 0.25)

    # Calculate the number of students who failed
    num_failed_students = num_remaining_students - num_b_or_c_students

    result = num_failed_students
    return result

print(solution())