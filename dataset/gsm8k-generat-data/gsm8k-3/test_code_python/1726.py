def solution():
    """At a certain school, 2/3 of the population are females. One-tenth of the males are foreign students. If the school has 300 students, how many students are non-foreign male students?"""
    # Define the proportion of females
    FEMALE_PROPORTION = 2/3

    # Calculate the number of female students
    female_students = round(FEMALE_PROPORTION * 300)

    # Calculate the number of male students
    male_students = 300 - female_students

    # Calculate the number of foreign male students
    foreign_male_students = round(male_students * 0.1)

    # Calculate the number of non-foreign male students
    non_foreign_male_students = male_students - foreign_male_students

    # Display the number of non-foreign male students
    result = non_foreign_male_students
    return result

print(solution())