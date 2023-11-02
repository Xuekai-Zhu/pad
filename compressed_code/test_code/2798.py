def solution():
    
    total_students = 800
    girls_ratio = 5/8
    boys_ratio = 1 - girls_ratio
    girls = girls_ratio * total_students
    boys = boys_ratio * total_students
    primary_grade_girls = 7/10 * girls
    primary_grade_boys = 2/5 * boys
    middle_school_girls = girls - primary_grade_girls
    middle_school_boys = boys - primary_grade_boys
    middle_schoolers = middle_school_girls + middle_school_boys
    result = middle_schoolers
    return result

print(solution())