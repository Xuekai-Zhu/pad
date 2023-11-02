def solution():
    """Three years from now, Tully will be twice as old as Kate. How old was Tully a year ago if Kate is now 29 years old?"""
    current_kate_age = 29
    tully_age_in_3_years = 2 * (current_kate_age + 3)
    current_tully_age = tully_age_in_3_years - 3
    tully_age_a_year_ago = current_tully_age - 1
    result = tully_age_a_year_ago
    return result

print(solution())