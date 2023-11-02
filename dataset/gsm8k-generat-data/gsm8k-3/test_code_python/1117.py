def solution():
    """The age of Gladys is equal to twice the sum of the ages of Billy and Lucas. Billy is 3 times younger than Gladys who is 30 years old now. How old will Lucas be three years from now?"""
    # Calculate Gladys' age
    gladys_age = 30
    billy_age = gladys_age / 3
    lucas_age = (gladys_age - 2 * (billy_age)) / 2

    # Calculate Lucas' age in three years
    lucas_age_in_3_years = lucas_age + 3

    # Display Lucas' age in three years
    result = lucas_age_in_3_years
    return result

print(solution())