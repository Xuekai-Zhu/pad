def solution():
    """The difference in age between Declan's elder son and younger son is 10 years. If the elder son is 40 years old now, how old will the younger son be 30 years from now?"""
    # Define the current age of the elder son and the age difference
    elder_age = 40
    age_difference = 10

    # Calculate the current age of the younger son
    younger_age = elder_age - age_difference

    # Calculate the age of the younger son 30 years from now
    younger_age_in_30_years = younger_age + 30

    # return the result
    result = younger_age_in_30_years
    return result

print(solution())