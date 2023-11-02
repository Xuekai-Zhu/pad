def solution():
    num_total_students = 200
    percent_female = 0.6
    percent_brunette_female = 0.5
    percent_short_brunette_female = 0.5

    # Calculate the number of female students
    num_female_students = num_total_students * percent_female

    # Calculate the number of female students who are brunette
    num_brunette_females = num_female_students * percent_brunette_female

    # Calculate the number of female, brunette students who are under 5 feet tall
    num_short_brunette_females = num_brunette_females * percent_short_brunette_female

    result = num_short_brunette_females
    return result

print(solution())