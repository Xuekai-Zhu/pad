def solution():
    total_students = 804
    passed_percentage = 0.75

    # Calculate the number of students who passed their exams
    num_passed = total_students * passed_percentage

    # Calculate the number of students who didn't pass their exams
    num_failed = total_students - num_passed
    result = num_failed
    return result

print(solution())