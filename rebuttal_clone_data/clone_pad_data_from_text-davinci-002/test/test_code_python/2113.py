def solution():
    total_students = 804
    percentage_passed = 75
    number_passed = total_students * (percentage_passed / 100)
    number_failed = total_students - number_passed
    result = number_failed
    return result

print(solution())