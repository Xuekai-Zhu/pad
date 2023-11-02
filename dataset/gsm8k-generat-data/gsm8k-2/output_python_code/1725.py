def solution():
    """At a certain school, 2/3 of the population are females. One-tenth of the males are foreign students. If the school has 300 students, how many students are non-foreign male students?"""
    total_students = 300
    female_students = round(total_students * (2/3))
    male_students = total_students - female_students
    foreign_male_students = round(male_students / 10)
    non_foreign_male_students = male_students - foreign_male_students
    result = non_foreign_male_students
    return result

print(solution())