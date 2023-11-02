def solution():
    """The age of Gladys is equal to twice the sum of the ages of Billy and Lucas. Billy is 3 times younger than Gladys who is 30 years old now. How old will Lucas be three years from now?"""
    gladys_age = 30
    billy_age = gladys_age / 3
    sum_of_billy_lucas_age = (gladys_age / 2) - billy_age
    lucas_age = sum_of_billy_lucas_age
    lucas_age_in_three_years = lucas_age + 3
    result = lucas_age_in_three_years
    return result

print(solution())