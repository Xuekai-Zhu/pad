def solution():
    total_students = 300  # total number of students
    female_students = (2/3) * total_students  # number of female students
    male_students = total_students - female_students  # number of male students
    foreign_male_students = male_students/10  # number of male foreign students
    non_foreign_male_students = male_students - foreign_male_students  # number of non-foreign male students
    result = non_foreign_male_students
    return result

print(solution())