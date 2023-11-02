def solution():
    """In a certain school, 2/3 of the male students like to play basketball, but only 1/5 of the female students like to play basketball. What percent of the population of the school do not like to play basketball if the ratio of the male to female students is 3:2 and there are 1000 students?"""
    total_students = 1000
    male_ratio = 3
    female_ratio = 2

    # calculate the number of male and female students using the ratio
    total_ratio = male_ratio + female_ratio
    num_male_students = int((male_ratio / total_ratio) * total_students)
    num_female_students = int((female_ratio / total_ratio) * total_students)

    # calculate the number of male and female students who like to play basketball
    num_male_basketball = int((2/3) * num_male_students)
    num_female_basketball = int((1/5) * num_female_students)

    # calculate the total number of students who do not like to play basketball
    num_not_basketball = total_students - num_male_basketball - num_female_basketball

    # calculate the percentage of the population that does not like to play basketball
    percent_not_basketball = (num_not_basketball / total_students) * 100

    result = percent_not_basketball
    return result

print(solution())