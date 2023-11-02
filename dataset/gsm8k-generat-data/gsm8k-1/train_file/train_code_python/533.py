def solution():
    """Jessica is six years older than Claire. In two years, Claire will be 20 years old. How old is Jessica now?"""
    claire_age_in_2_years = 20
    claire_current_age = claire_age_in_2_years - 2
    jessica_current_age = claire_current_age + 6
    result = jessica_current_age
    return result

print(solution())