def solution():
    """Three years ago, Bethany was twice the age of her younger sister. In 5 years, her younger sister will be 16. How old is Bethany now?"""
    younger_sister_in_5_years = 16
    younger_sister_age_now = younger_sister_in_5_years - 5
    bethany_age_three_years_ago = younger_sister_age_now * 2
    bethany_age_now = bethany_age_three_years_ago + 3 + 3 # adding 3 years for the age difference
    result = bethany_age_now
    return result

print(solution())