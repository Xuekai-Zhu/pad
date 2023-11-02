def solution():
    # Find the age of the hyena
    age_hyena = 12 / 2

    # Find the age of the baby lioness and baby hyena
    age_baby_lioness = 12 / 2
    age_baby_hyena = age_hyena / 2

    # Calculate the sum of the age of the babies in five years
    sum_age_babies = (age_baby_lioness + age_baby_hyena) * 2 + 5
    result = sum_age_babies
    return result

print(solution())