def solution():
    """Two years ago, Jared was twice as old as Tom. If Tom will be 30 in five years, how old is Jared now?"""
    tom_age_in_2_years = 30 - 5 - 2
    jared_age_in_2_years = 2 * tom_age_in_2_years
    jared_current_age = jared_age_in_2_years + 2
    result = jared_current_age
    return result

print(solution())