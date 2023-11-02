def solution():
    # Calculate the age of the hyena
    hyena_age = 12 / 2

    # Calculate the age of the lioness's baby
    lioness_baby_age = 12 / 2

    # Calculate the age of the hyena's baby
    hyena_baby_age = hyena_age / 2

    # Calculate the sum of the ages of the babies in 5 years
    sum_babies_age_in_5_years = 5 * (lioness_baby_age + hyena_baby_age)

    result = sum_babies_age_in_5_years
    return result

print(solution())