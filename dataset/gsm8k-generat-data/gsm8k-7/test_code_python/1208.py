def solution():
    lioness_age = 12
    hyena_age = lioness_age / 2
    lioness_baby_age = lioness_age / 2
    hyena_baby_age = hyena_age / 2

    total_babies_age = (lioness_baby_age + hyena_baby_age) * 2
    total_babies_age_in_5_years = total_babies_age + (5 * 2)

    result = total_babies_age_in_5_years
    return result

print(solution())