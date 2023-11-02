def solution():
    """The average of marks scored in four tests by Jake was 75. If Jake scored 80 marks in the first test and 10 more in the second test, and an equal number of marks in the third and fourth test, calculate the marks he scored in the third test."""
    # Calculate the total marks scored in the four tests
    total_marks = 75 * 4

    # Calculate the marks scored in the first two tests
    first_test_marks = 80
    second_test_marks = first_test_marks + 10

    # Calculate the total marks scored in the first two tests
    first_two_tests_total = first_test_marks + second_test_marks

    # Calculate the marks scored in the third and fourth tests
    third_test_marks = (total_marks - first_two_tests_total) / 2

    # Display the marks scored in the third test
    result = third_test_marks
    return result

print(solution())