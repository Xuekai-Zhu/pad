def solution():
    # Calculate the total marks scored by Jake in the four tests
    total_marks = 75 * 4  # since the average of four tests is 75

    # Calculate the marks scored by Jake in the second, third, and fourth tests
    marks_second_test = 80 + 10  # he scored 80 marks in the first test and 10 more in the second test
    marks_third_test = (total_marks - marks_second_test - marks_second_test) / 2  # equal marks in third and fourth tests

    result = marks_third_test
    return result

print(solution())