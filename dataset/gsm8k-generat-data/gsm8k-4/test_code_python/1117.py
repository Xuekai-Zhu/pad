def solution():
    """The age of Gladys is equal to twice the sum of the ages of Billy and Lucas. Billy is 3 times younger than Gladys who is 30 years old now. How old will Lucas be three years from now?"""
    # Define Gladys' age and the age ratio between her and Billy
    gladys_age = 30
    gladys_billy_ratio = 3

    # Calculate Billy's age
    billy_age = gladys_age / gladys_billy_ratio

    # Calculate the sum of Billy and Lucas' ages
    billy_lucas_sum = (gladys_age / 2) - billy_age

    # Calculate Lucas' current age
    lucas_age = billy_lucas_sum

    # Calculate Lucas' age three years from now
    lucas_age_three_years = lucas_age + 3

    # return the result
    result = lucas_age_three_years
    return result

print(solution())