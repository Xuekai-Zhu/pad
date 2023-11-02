def solution():
    fem_age = 11  # Fem is currently 11 years old
    matt_age = fem_age * 4  # Matt is four times as old as Fem

    # Calculate the sum of ages in two years
    fem_age_in_two_years = fem_age + 2
    matt_age_in_two_years = matt_age + 2
    total_age_in_two_years = fem_age_in_two_years + matt_age_in_two_years
    result = total_age_in_two_years
    return result

print(solution())