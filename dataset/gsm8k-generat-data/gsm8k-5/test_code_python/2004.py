def solution():
    # Calculate the total marks scored in the four tests
    total_marks = 75 * 4

    # Calculate the marks scored in the second test
    second_test_marks = 80 + 10

    # Calculate the marks scored in the first and second tests combined
    first_second_marks = 80 + second_test_marks

    # Calculate the marks scored in the third and fourth tests combined
    third_fourth_marks = total_marks - first_second_marks

    # Calculate the marks scored in each of the third and fourth tests
    third_test_marks = third_fourth_marks / 2
    result = third_test_marks
    return result

print(solution())