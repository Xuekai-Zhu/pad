def solution():
    """Three years from now, Tully will be twice as old as Kate. How old was Tully a year ago if Kate is now 29 years old?"""
    # Define Kate's age
    kate_age = 29

    # Calculate Tully's age three years from now
    tully_age_in_3_years = kate_age * 2

    # Calculate Tully's age now
    tully_age_now = tully_age_in_3_years - 3

    # Calculate Tully's age a year ago
    tully_age_1_year_ago = tully_age_now - 1

    result = tully_age_1_year_ago
    return result

print(solution())