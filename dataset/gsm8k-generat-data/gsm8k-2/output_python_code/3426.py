def solution():
    """In four years, Annika will be three times as old as Hans. If Hans is now 8 years old, how old is Annika now?"""
    hans_age = 8
    annika_age_in_4_years = 3 * hans_age + 4
    annika_age_now = annika_age_in_4_years - 4
    result = annika_age_now
    return result

print(solution())