def solution():
    
    total_marks = 75 * 4
    marks_first_test = 80
    marks_second_test = 80 + 10
    average_marks_third_fourth_test = total_marks - marks_first_test - marks_second_test
    marks_each_third_fourth_test = average_marks_third_fourth_test / 2
    result = marks_each_third_fourth_test
    return result

print(solution())