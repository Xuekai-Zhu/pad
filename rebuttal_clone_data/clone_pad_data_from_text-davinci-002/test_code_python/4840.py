def solution():
    donuts_baked = 4 * 12
    students_in_class = 30
    students_who_like_donuts = students_in_class * 0.80
    donuts_per_student = donuts_baked / students_who_like_donuts
    result = donuts_per_student
    return result

print(solution())