def solution():
    """40 less than 10 times Diaz's age is 20 more than 10 times Sierra's age. If Sierra is currently 30 years old, how old will Diaz be 20 years from now?"""
    sierra_age = 30
    diaz_age = ((20 + (10 * sierra_age) + 40)/10)
    diaz_age_in_20_years = diaz_age + 20
    result = diaz_age_in_20_years
    return result

print(solution())