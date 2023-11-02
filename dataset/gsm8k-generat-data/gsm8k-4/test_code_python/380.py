def solution():
    """Patrick is half the age of his elder brother Robert. If Robert will turn 30 after 2 years, how old is Patrick now?"""
    # Define Robert's age in 2 years
    robert_age_in_2_years = 30

    # Calculate Robert's current age
    robert_current_age = robert_age_in_2_years - 2

    # Calculate Patrick's current age
    patrick_current_age = robert_current_age / 2

    # Return Patrick's current age
    result = patrick_current_age
    return result

print(solution())