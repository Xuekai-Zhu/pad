def solution():
    # Calculate how old the mother was 5 years ago
    mother_age_5_years_ago = 41 - 5  # Mother is currently 41 years old

    # Calculate how old the daughter was 5 years ago
    daughter_age_5_years_ago = mother_age_5_years_ago / 2

    # Calculate how old the daughter is currently
    daughter_age_now = daughter_age_5_years_ago + 5

    # Calculate how old the daughter will be in 3 years
    daughter_age_in_3_years = daughter_age_now + 3
    result = daughter_age_in_3_years
    return result

print(solution())