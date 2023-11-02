def solution():
    """At a certain school, 2/3 of the population are females. One-tenth of the males are foreign students. If the school has 300 students, how many students are non-foreign male students?"""
    # Define the total number of students
    total_students = 300

    # Calculate the number of female students
    female_students = total_students * (2/3)

    # Calculate the number of male students
    male_students = total_students - female_students

    # Calculate the number of male foreign students
    male_foreign_students = male_students * (1/10)

    # Calculate the number of non-foreign male students
    male_nonforeign_students = male_students - male_foreign_students

    # Return the result
    result = male_nonforeign_students
    return result

print(solution())