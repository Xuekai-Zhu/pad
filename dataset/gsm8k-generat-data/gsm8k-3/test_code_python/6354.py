def solution():
    """Nick is 13 years old. His sister is 6 years older and their brother is half their combined age. How old would their brother be in 5 years?"""
    # Nick's age
    nick_age = 13

    # Sister's age
    sister_age = nick_age + 6

    # Combined age of Nick and Sister
    combined_age = nick_age + sister_age

    # Brother's age
    brother_age = combined_age / 2

    # Brother's age in 5 years
    brother_age_5_years = brother_age + 5

    result = brother_age_5_years
    return result

print(solution())