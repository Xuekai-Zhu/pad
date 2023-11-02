def solution():
    """Eustace is twice as old as Milford. In 3 years, he will be 39. How old will Milford be?"""
    eustace_age = 39 - 3  # Eustace's current age
    milford_age = eustace_age / 2
    milford_age_in_3_years = milford_age + 3
    result = milford_age_in_3_years
    return result

print(solution())