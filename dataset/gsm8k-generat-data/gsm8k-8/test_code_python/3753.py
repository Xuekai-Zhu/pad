def solution():
    # Calculate the number of students who passed their exams
    passed = 0.75 * 804

    # Calculate the number of students who didn't pass their exams
    did_not_pass = 804 - passed
    result = did_not_pass
    return result

print(solution())