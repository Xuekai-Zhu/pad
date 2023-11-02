def solution():
    buns_per_package = 8
    packages_bought = 30
    total_buns = packages_bought * buns_per_package
    students_per_class = 30
    total_students = students_per_class * 4
    buns_per_student = total_buns / total_students
    
    return buns_per_student

print(solution())