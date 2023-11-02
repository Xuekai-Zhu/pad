def solution():
    """In today's field day challenge, the 4th graders were competing against the 5th graders. Each grade had 2 different classes. The first 4th grade class had 12 girls and 13 boys. The second 4th grade class had 15 girls and 11 boys. The first 5th grade class had 9 girls and 13 boys while the second 5th grade class had 10 girls and 11 boys. In total, how many more boys were competing than girls?"""
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