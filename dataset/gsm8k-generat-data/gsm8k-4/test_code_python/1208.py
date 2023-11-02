def solution():
    """The age of a lioness in a park is twice the age of a hyena in the same park. 
    The lioness is 12 years old. If the babies of the two animals are half the age of their mothers, 
    calculate the sum of the age of the babies in five years."""
    # Define the age of the lioness
    lioness_age = 12

    # Calculate the age of the hyena
    hyena_age = lioness_age / 2

    # Calculate the age of the baby lion
    baby_lion_age = lioness_age / 2

    # Calculate the age of the baby hyena
    baby_hyena_age = hyena_age / 2

    # Calculate the sum of the ages of the babies in five years
    sum_of_babies_age_in_five_years = (baby_lion_age + 5) + (baby_hyena_age + 5)

    # Return the result
    result = sum_of_babies_age_in_five_years
    return result

print(solution())