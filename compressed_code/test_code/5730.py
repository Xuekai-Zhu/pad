def solution():
    
    fourth_grade_class1_boys = 13
    fourth_grade_class1_girls = 12
    fourth_grade_class2_boys = 11
    fourth_grade_class2_girls = 15
    fifth_grade_class1_boys = 13
    fifth_grade_class1_girls = 9
    fifth_grade_class2_boys = 11
    fifth_grade_class2_girls = 10
    
    total_boys = fourth_grade_class1_boys + fourth_grade_class2_boys + fifth_grade_class1_boys + fifth_grade_class2_boys
    total_girls = fourth_grade_class1_girls + fourth_grade_class2_girls + fifth_grade_class1_girls + fifth_grade_class2_girls
    
    difference = total_boys - total_girls
    
    result = difference
    
    return result

print(solution())