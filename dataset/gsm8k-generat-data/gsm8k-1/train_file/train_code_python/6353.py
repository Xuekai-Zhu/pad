def solution():
    """Nick is 13 years old. His sister is 6 years older and their brother is half their combined age. How old would their brother be in 5 years?"""
    nick_age = 13
    sister_age = nick_age + 6
    combined_age = nick_age + sister_age
    brother_age = combined_age / 2
    brother_age_in_5_years = brother_age + 5
    result = brother_age_in_5_years
    return result

print(solution())