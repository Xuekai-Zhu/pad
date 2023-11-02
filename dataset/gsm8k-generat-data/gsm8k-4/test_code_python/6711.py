def solution():
    """40 less than 10 times Diaz's age is 20 more than 10 times Sierra's age. If Sierra is currently 30 years old, how old will Diaz be 20 years from now?"""
    # Define Sierra's current age
    sierra_age = 30

    # Calculate the equation in terms of Diaz's age
    diaz_age = (20 + 10 * sierra_age + 40) / 10

    # Calculate Diaz's age in 20 years
    diaz_age_20_years = diaz_age + 20

    # return the result
    result = diaz_age_20_years
    return result

print(solution())