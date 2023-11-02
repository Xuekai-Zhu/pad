def solution():
    ron_age_after_five_years = 43 + 5  # Ron will be 43 + 5 = 48 years old after five years
    ron_age_now = 43  # Ron's current age is 43 years old
    maurice_age_after_five_years = ron_age_after_five_years / 4  # After five years, Ron will be four times as old as Maurice
    maurice_age_now = maurice_age_after_five_years - 5  # Maurice is 5 years younger than Ron

    result = maurice_age_now
    return result

print(solution())