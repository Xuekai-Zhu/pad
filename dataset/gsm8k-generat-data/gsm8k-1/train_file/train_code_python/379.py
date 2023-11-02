def solution():
    """Patrick is half the age of his elder brother Robert. If Robert will turn 30 after 2 years, how old is Patrick now?"""
    robert_age_after_2_years = 30
    robert_current_age = robert_age_after_2_years - 2
    patrick_current_age = robert_current_age / 2
    result = patrick_current_age
    return result

print(solution())