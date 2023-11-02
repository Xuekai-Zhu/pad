def solution():
    """Eustace is twice as old as Milford. In 3 years, he will be 39. How old will Milford be?"""
    eustace_age_in_3_years = 39
    eustace_age_now = eustace_age_in_3_years - 3
    milford_age_now = eustace_age_now / 2
    milford_age_in_3_years = milford_age_now + 3
    result = milford_age_in_3_years
    return result

print(solution())