def solution():
    total_students = 300  # The school has 300 students
    female_population = (2/3) * total_students  # 2/3 of the population are females
    male_population = total_students - female_population  # The rest of the population are males

    # Calculate the number of male foreign students
    male_foreign_students = (1/10) * male_population

    # Calculate the number of non-foreign male students
    non_foreign_male_students = male_population - male_foreign_students
    result = non_foreign_male_students
    return result

print(solution())