def solution():
    # Calculate the sum of marks scored in all four tests
    total_marks = 75 * 4

    # Calculate the sum of marks scored in the first two tests
    first_two_marks = 80 + (80 + 10)

    # Calculate the marks scored in the third and fourth test combined
    third_fourth_marks = total_marks - first_two_marks

    # Divide the marks equally between the third and fourth test
    third_test_marks = third_fourth_marks / 2

    result = third_test_marks
    return result

print(solution())