def solution():
    total_students = 300
    female_population = 2/3 * total_students
    male_population = total_students - female_population
    foreign_male_students = 1/10 * male_population
    non_foreign_male_students = male_population - foreign_male_students
    result = non_foreign_male_students
    return result

print(solution())