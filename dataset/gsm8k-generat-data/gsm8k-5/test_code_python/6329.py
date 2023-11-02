def solution():
    # Total number of students in the group
    total_students = 3 * 8  # Divided into 3 groups of 8

    # Number of students who left early
    students_left_early = 2

    # Calculate the number of students remaining
    students_remaining = total_students - students_left_early
    result = students_remaining
    return result

print(solution())