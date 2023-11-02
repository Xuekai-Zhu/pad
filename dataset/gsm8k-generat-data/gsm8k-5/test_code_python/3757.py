def solution():
    heath_age_in_5_years = 16 + 5  # In 5 years, Heath will be 16+5=21 years old
    jude_age_in_5_years = heath_age_in_5_years / 3  # In 5 years, Heath will be 3 times as old as Jude
    jude_age_today = jude_age_in_5_years - 5  # Jude's age today is 5 years less than his age in 5 years

    result = jude_age_today
    return result

print(solution())