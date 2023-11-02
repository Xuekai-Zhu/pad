def solution():
    """Matt is four times as old as Fem. Currently, Fem is 11 years old. In two years, what is the sum of the ages of Matt and Fem?"""
    # Current age of Fem
    fem_age = 11

    # Calculate Matt's current age
    matt_age = 4 * fem_age

    # Calculate their ages in two years
    fem_age_in_2 = fem_age + 2
    matt_age_in_2 = matt_age + 2

    # Calculate the sum of their ages in two years
    sum_of_ages_in_2 = fem_age_in_2 + matt_age_in_2

    # Display the sum of their ages in two years
    result = sum_of_ages_in_2
    return result

print(solution())