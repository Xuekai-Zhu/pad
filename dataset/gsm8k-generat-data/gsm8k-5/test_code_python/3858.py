def solution():
    sister_age_in_5_years = 16  # Bethany's younger sister will be 16 in 5 years
    sister_age_3_years_ago = sister_age_in_5_years - 5 - 3  # Calculate her sister's age 3 years ago
    bethany_age_3_years_ago = sister_age_3_years_ago * 2  # Bethany was twice her sister's age 3 years ago

    # Calculate Bethany's current age
    bethany_age = bethany_age_3_years_ago + 3
    result = bethany_age
    return result

print(solution())