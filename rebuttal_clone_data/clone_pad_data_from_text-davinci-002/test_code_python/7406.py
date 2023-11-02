def solution():
    fourth_grade_class_one = 12
    fourth_grade_class_two = 15
    fifth_grade_class_one = 9
    fifth_grade_class_two = 10
    fourth_grade_total = fourth_grade_class_one + fourth_grade_class_two
    fifth_grade_total = fifth_grade_class_one + fifth_grade_class_two
    total_girls = fourth_grade_total + fifth_grade_total
    fourth_grade_boys = 13
    fifth_grade_boys = 13
    total_boys = fourth_grade_boys + fifth_grade_boys
    more_boys = total_boys - total_girls
    result = more_boys
    
    return result

print(solution())