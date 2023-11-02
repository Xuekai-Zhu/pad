def solution():
    initial_grade = 78  # Brittany got a 78 on her first test
    average_grade = 81  # Her average after the second test is an 81
    num_tests = 2  # She has taken two tests in total

    # Calculate the total score she needs on both tests to get an average of 81
    required_total = average_grade * num_tests

    # Calculate the score she got on the second test
    second_test_grade = required_total - initial_grade
    result = second_test_grade
    return result

print(solution())