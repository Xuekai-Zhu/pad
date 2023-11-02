def solution():
    """
    In today's field day challenge, the 4th graders were competing against the 5th graders. Each grade had 2 different classes. 
    The first 4th grade class had 12 girls and 13 boys. The second 4th grade class had 15 girls and 11 boys. 
    The first 5th grade class had 9 girls and 13 boys while the second 5th grade class had 10 girls and 11 boys. 
    In total, how many more boys were competing than girls?
    """
    girls_4th_grade = 12 + 15
    boys_4th_grade = 13 + 11
    girls_5th_grade = 9 + 10
    boys_5th_grade = 13 + 11
    total_girls = girls_4th_grade + girls_5th_grade
    total_boys = boys_4th_grade + boys_5th_grade
    more_boys = total_boys - total_girls
    result = more_boys
    return result

print(solution())