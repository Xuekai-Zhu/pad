def solution():
    """Matt is four times as old as Fem. Currently, Fem is 11 years old. In two years, what is the sum of the ages of Matt and Fem?"""
    # Define Fem's current age
    fem_age = 11

    # Calculate Matt's current age
    matt_age = fem_age * 4

    # Calculate Fem's age in two years
    fem_age_in_2_years = fem_age + 2

    # Calculate Matt's age in two years
    matt_age_in_2_years = matt_age + 2

    # Calculate the sum of their ages in two years
    sum_of_ages_in_2_years = fem_age_in_2_years + matt_age_in_2_years

    # Return the result
    result = sum_of_ages_in_2_years
    return result

print(solution())