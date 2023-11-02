def solution():
    """Brittany got a 78 on her first test. After her second test, her average rose to an 81. What grade did she get on her second test?"""
    first_test_grade = 78
    target_average = 81
    second_test_grade = (target_average * 2) - first_test_grade
    result = second_test_grade
    return result

print(solution())