def solution():
    age_tom_in_5_years = 30  # Tom will be 30 in 5 years
    age_tom_now = age_tom_in_5_years - 5  # Tom's current age
    age_jared_two_years_ago = age_tom_now * 2  # Two years ago, Jared was twice as old as Tom
    age_jared_now = age_jared_two_years_ago + 2  # Jared's current age

    result = age_jared_now
    return result

print(solution())