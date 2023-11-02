def solution():
    """In a certain school, 2/3 of the male students like to play basketball, but only 1/5 of the female students like to play basketball. What percent of the population of the school do not like to play basketball if the ratio of the male to female students is 3:2 and there are 1000 students?"""
    # Define the ratio of male to female students
    ratio = 3/2

    # Calculate the number of male students
    num_male = (3/5) * 1000

    # Calculate the number of female students
    num_female = (2/5) * 1000

    # Calculate the number of male students who like basketball
    num_male_basketball = (2/3) * num_male

    # Calculate the number of female students who like basketball
    num_female_basketball = (1/5) * num_female

    # Calculate the number of students who do not like basketball
    num_no_basketball = 1000 - num_male_basketball - num_female_basketball

    # Calculate the percentage of students who do not like basketball
    percent_no_basketball = (num_no_basketball / 1000) * 100

    # Display the percentage of students who do not like basketball
    result = percent_no_basketball
    return result

print(solution())