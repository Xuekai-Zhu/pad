def solution():
    total_students = 1000

    # Calculate the number of male students
    num_male_students = (3 / 5) * total_students

    # Calculate the number of female students
    num_female_students = (2 / 5) * total_students

    # Calculate the number of male students who like basketball
    num_male_basketball = (2 / 3) * num_male_students

    # Calculate the number of female students who like basketball
    num_female_basketball = (1 / 5) * num_female_students

    # Calculate the total number of students who do not like basketball
    num_not_like_basketball = total_students - num_male_basketball - num_female_basketball

    # Calculate the percentage of the population that does not like basketball
    percent_not_like_basketball = (num_not_like_basketball / total_students) * 100
    result = percent_not_like_basketball
    return result

print(solution())