def solution():
    
    semesters = 8
    total_credits = 120
    credits_per_class = 3
    classes_per_semester = (total_credits / semesters) / credits_per_class
    result = classes_per_semester
    return result

print(solution())