def solution():
    """In 5 years, Heath will be 3 times as old as Jude. If Heath is 16 years old today, how old is Jude today?"""
    heath_age_now = 16
    jude_age_in_5_years = heath_age_now * (1/3)
    jude_age_now = jude_age_in_5_years - 5
    result = jude_age_now
    return result

print(solution())