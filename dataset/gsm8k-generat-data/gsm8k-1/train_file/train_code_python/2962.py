def solution():
    """Three years from now, Tully will be twice as old as Kate. How old was Tully a year ago if Kate is now 29 years old?"""
    current_age_kate = 29
    years_from_now = 3
    tully_age_in_three_years = current_age_kate * 2
    tully_current_age = tully_age_in_three_years - years_from_now
    tully_age_a_year_ago = tully_current_age - 1
    result = tully_age_a_year_ago
    return result

print(solution())