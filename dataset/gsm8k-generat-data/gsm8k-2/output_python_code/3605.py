def solution():
    """In a school with 800 students, 5/8 of the students are girls. Seven-tenths of the girls and two-fifths of the boys are in the primary grades, while the rest are middle schoolers. How many middle schoolers are there?"""
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