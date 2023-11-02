def solution():
    total_students = 804  # Total number of senior high school students
    passed_percentage = 75  # Percentage of students who passed

    # Calculate the number of students who passed their exams
    passed_students = int(total_students * (passed_percentage / 100))

    # Calculate the number of students who did not pass their exams
    failed_students = total_students - passed_students
    result = failed_students
    return result

print(solution())