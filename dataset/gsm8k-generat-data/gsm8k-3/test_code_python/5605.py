def solution():
    """Two years ago, Jared was twice as old as Tom. If Tom will be 30 in five years, how old is Jared now?"""
    # Determine Tom's current age
    tom_age = 30 - 5

    # Determine how old Jared was two years ago
    jared_two_years_ago = tom_age * 2

    # Determine Jared's current age
    jared_age = jared_two_years_ago + 2

    # Display Jared's current age
    result = jared_age
    return result

print(solution())