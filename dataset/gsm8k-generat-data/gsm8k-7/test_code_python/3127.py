def solution():
    fem_age = 11
    matt_age = 4 * fem_age

    # In two years, Fem will be 13 and Matt will be 4*11 + 2 = 46 years old
    fem_age_in_2_years = fem_age + 2
    matt_age_in_2_years = matt_age + 2

    # Calculate the sum of their ages in two years
    total_age_in_2_years = fem_age_in_2_years + matt_age_in_2_years
    result = total_age_in_2_years
    return result

print(solution())