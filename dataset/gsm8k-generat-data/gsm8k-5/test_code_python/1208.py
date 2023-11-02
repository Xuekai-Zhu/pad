def solution():
    lioness_age = 12  # The lioness is 12 years old
    hyena_age = lioness_age / 2  # The hyena is half the age of the lioness

    # Calculate the age of the babies of both animals
    lioness_baby_age = lioness_age / 2  # The lioness's baby is half her age
    hyena_baby_age = hyena_age / 2  # The hyena's baby is half her age

    # Calculate the sum of the ages of the babies in 5 years
    total_age = (lioness_baby_age + hyena_baby_age) * 2  # Double the sum to account for both babies
    total_age_in_five_years = total_age + (5 * 2)  # Add 5 years to each baby's age and double the sum again

    result = total_age_in_five_years
    return result

print(solution())