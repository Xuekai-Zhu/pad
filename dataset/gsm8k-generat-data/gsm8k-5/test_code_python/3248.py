def solution():
    total_students = 180  # Total number of students in ninth grade
    bombed_students = total_students * (1/4)  # Number of students who bombed their finals
    remaining_students = total_students - bombed_students  # Number of students remaining
    absent_students = remaining_students * (1/3)  # Number of students who didn't show up for the test
    failed_students = 20  # Number of students who got less than a D
    passed_students = remaining_students - absent_students - failed_students  # Number of students who passed their finals

    result = passed_students
    return result

print(solution())