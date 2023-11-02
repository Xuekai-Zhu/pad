def solution():
    
    total_marks = 75 * 4
    marks_first_test = 80
    marks_second_test = 80 + 10
    marks_third_test = (total_marks - marks_first_test - marks_second_test) / 2
    result = marks_third_test
    return result

print(solution())