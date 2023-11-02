def solution():
    total_students = 800
    girls = (5/8) * total_students
    boys = total_students - girls
    girls_primary = (7/10) * girls
    boys_primary = (2/5) * boys
    primary_students = girls_primary + boys_primary
    middle_school_students = total_students - primary_students
    result = middle_school_students
    return result

print(solution())