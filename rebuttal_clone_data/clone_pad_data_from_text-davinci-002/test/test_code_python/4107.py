def solution():
    semesters = 8
    credits_needed = 120
    credits_per_class = 3
    classes_per_semester = credits_needed / (semesters * credits_per_class)
    result = classes_per_semester
    return result

print(solution())