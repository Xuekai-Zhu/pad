def solution():
    """The age of a lioness in a park is twice the age of a hyena in the same park. The lioness is 12 years old. If the babies of the two animals are half the age of their mothers, calculate the sum of the age of the babies in five years."""
    lioness_age = 12
    hyena_age = lioness_age / 2
    lioness_baby_age = lioness_age / 2
    hyena_baby_age = hyena_age / 2
    total_baby_age_in_five_years = (lioness_baby_age + hyena_baby_age) * 2 + 5
    result = total_baby_age_in_five_years
    return result

print(solution())