def solution():
    """The difference in ages between Richard and Hurley is 20. If Hurley is 14 years old, what are their combined ages 40 years from now?"""
    hurley_age = 14
    richard_age = hurley_age + 20
    combined_age_now = hurley_age + richard_age
    combined_age_40_years = combined_age_now + 40 * 2
    result = combined_age_40_years
    return result

print(solution())