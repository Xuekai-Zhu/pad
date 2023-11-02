def solution():
    """The average of marks scored in four tests by Jake was 75. If jake scored 80 marks in the first test and 10 more in the second test, and an equal number of marks in the third and fourth test, calculate the marks he scored in the third test."""
    total_marks = 75 * 4
    marks_first_test = 80
    marks_second_test = 80 + 10
    average_marks_third_fourth_test = total_marks - marks_first_test - marks_second_test
    marks_each_third_fourth_test = average_marks_third_fourth_test / 2
    result = marks_each_third_fourth_test
    return result

print(solution())