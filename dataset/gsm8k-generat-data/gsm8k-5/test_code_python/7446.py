def solution():
    # Calculate the number of male and female students
    total_students = 1000
    male_ratio = 3
    female_ratio = 2
    male_students = (male_ratio / (male_ratio + female_ratio)) * total_students
    female_students = (female_ratio / (male_ratio + female_ratio)) * total_students

    # Calculate the number of male and female students who like to play basketball
    male_basketball = (2/3) * male_students
    female_basketball = (1/5) * female_students

    # Calculate the total number of students who do not like to play basketball
    no_basketball = total_students - male_basketball - female_basketball

    # Calculate the percentage of the population who do not like to play basketball
    percentage_no_basketball = (no_basketball / total_students) * 100
    result = percentage_no_basketball
    return result

print(solution())