def solution():
    """Three years ago, Bethany was twice the age of her younger sister. In 5 years, her younger sister will be 16. How old is Bethany now?"""
    sister_age_in_5_years = 16
    sister_age_three_years_ago = sister_age_in_5_years - 5 - 3
    bethany_age_three_years_ago = sister_age_three_years_ago * 2
    bethany_age_now = bethany_age_three_years_ago + 3 + 3
    result = bethany_age_now
    return result

print(solution())