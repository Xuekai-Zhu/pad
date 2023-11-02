def solution():
    # Calculate the number of students who passed their exams
    passed_students = 0.75 * 804
    
    # Calculate the number of students who didn't pass their exams
    failed_students = 804 - passed_students
    
    result = failed_students
    return result

print(solution())