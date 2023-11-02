def solution():
    total_students = 300
    female_ratio = 2/3
    male_ratio = 1 - female_ratio
    foreign_male_ratio = 1/10

    # Calculate the number of female students
    num_female = total_students * female_ratio

    # Calculate the number of male students
    num_male = total_students * male_ratio

    # Calculate the number of foreign male students
    num_foreign_male = num_male * foreign_male_ratio

    # Calculate the number of non-foreign male students
    num_non_foreign_male = num_male - num_foreign_male
    result = num_non_foreign_male
    return result

print(solution())