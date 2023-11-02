def solution():
    kate_age = 29  # Kate is currently 29 years old
    tully_age_in_3_years = 2 * (kate_age + 3)  # Tully will be twice Kate's age in 3 years
    tully_age_now = tully_age_in_3_years - 3  # Subtract 3 years to get Tully's current age
    tully_age_a_year_ago = tully_age_now - 1  # Subtract 1 year to get Tully's age a year ago
    result = tully_age_a_year_ago
    return result

print(solution())