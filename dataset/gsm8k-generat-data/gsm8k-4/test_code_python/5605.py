def solution():
    """Two years ago, Jared was twice as old as Tom. If Tom will be 30 in five years, how old is Jared now?"""
    # Calculate Tom's current age
    tom_age = 30 - 5
    # Tom's age 2 years ago
    tom_age_two_years_ago = tom_age - 2

    # Calculate Jared's age 2 years ago
    jared_age_two_years_ago = tom_age_two_years_ago * 2

    # Calculate Jared's current age
    jared_age = jared_age_two_years_ago + 2

    # Return the result
    result = jared_age
    return result

print(solution())