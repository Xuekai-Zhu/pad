def solution():
    """In a certain school, 2/3 of the male students like to play basketball, but only 1/5 of the female students like to play basketball. What percent of the population of the school do not like to play basketball if the ratio of the male to female students is 3:2 and there are 1000 students?"""
    # Define the total number of students and the ratio of male to female students
    total_students = 1000
    male_to_female_ratio = 3/2

    # Calculate the number of male and female students
    male_students = total_students * (male_to_female_ratio / (1 + male_to_female_ratio))
    female_students = total_students - male_students

    # Calculate the number of male and female students who like to play basketball
    male_basketball = male_students * (2/3)
    female_basketball = female_students * (1/5)

    # Calculate the total number of students who do not like to play basketball
    not_interested = total_students - male_basketball - female_basketball

    # Calculate the percentage of students who do not like to play basketball
    not_interested_percentage = (not_interested / total_students) * 100

    # return the result
    result = not_interested_percentage
    return result

print(solution())