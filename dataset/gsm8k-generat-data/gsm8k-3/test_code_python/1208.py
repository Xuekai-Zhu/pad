def solution():
    """The age of a lioness in a park is twice the age of a hyena in the same park. The lioness is 12 years old. If the babies of the two animals are half the age of their mothers, calculate the sum of the age of the babies in five years."""
    # Calculate the age of the hyena
    hyena_age = 12 / 2

    # Calculate the age of the hyena's baby
    hyena_baby_age = hyena_age / 2

    # Calculate the age of the lioness's baby
    lioness_baby_age = 12 / 2

    # Calculate the sum of the ages of the babies in five years
    sum_of_babies_age = (hyena_baby_age + lioness_baby_age) * 2 + 5

    # Display the result
    result = sum_of_babies_age
    return result

print(solution())