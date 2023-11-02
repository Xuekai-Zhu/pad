def solution():
    # Define the current grade and number of tests taken
    current_grade = (95 + 80) / 2
    tests_taken = 2

    # Define the desired average and number of total tests
    desired_average = 90
    total_tests = 3

    # Calculate the minimum score needed on the third test
    min_third_test_score = (desired_average * total_tests) - (current_grade * tests_taken)
    result = min_third_test_score
    return result

print(solution())