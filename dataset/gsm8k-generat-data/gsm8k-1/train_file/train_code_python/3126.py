def solution():
    """Matt is four times as old as Fem. Currently, Fem is 11 years old. In two years, what is the sum of the ages of Matt and Fem?"""
    fem_age = 11
    matt_age = fem_age * 4
    fem_age_in_2_years = fem_age + 2
    matt_age_in_2_years = matt_age + 2
    total_age_in_2_years = fem_age_in_2_years + matt_age_in_2_years
    result = total_age_in_2_years
    return result

print(solution())