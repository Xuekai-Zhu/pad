def solution():
    average_marks = 75
    marks_first_test = 80
    marks_second_test = marks_first_test + 10
    total_marks = average_marks * 4

    # Calculate the total marks scored in the first two tests
    total_marks_first_two_tests = marks_first_test + marks_second_test

    # Calculate the marks scored in the third and fourth tests combined
    total_marks_third_and_fourth_tests = total_marks - total_marks_first_two_tests

    # Calculate the marks scored in the third test
    marks_third_test = total_marks_third_and_fourth_tests / 2
    result = marks_third_test
    return result

print(solution())