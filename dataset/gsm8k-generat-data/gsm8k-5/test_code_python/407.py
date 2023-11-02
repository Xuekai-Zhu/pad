def solution():
    age_difference = 3  # In 3 years, Eustace will be 39
    eustace_age = 39 - age_difference  # Current age of Eustace
    milford_age = eustace_age / 2  # Eustace is twice as old as Milford

    # Age of Milford in 3 years
    milford_age_3_years_later = milford_age + age_difference

    result = milford_age_3_years_later
    return result

print(solution())