def solution():
    sister_age_5_years_from_now = 16
    younger_sister_age = sister_age_5_years_from_now - 5

    # Calculate the age of Bethany 3 years ago
    bethany_age_3_years_ago = (younger_sister_age * 2) - 3

    # Calculate Bethany's current age
    bethany_age = bethany_age_3_years_ago + 3 + 3  # adding 3 years for the time elapsed
    result = bethany_age
    return result

print(solution())