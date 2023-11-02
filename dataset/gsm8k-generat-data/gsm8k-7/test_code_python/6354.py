def solution():
    nick_age = 13
    sister_age = nick_age + 6
    combined_age = nick_age + sister_age
    brother_age = combined_age / 2

    # Calculate how old their brother will be in 5 years
    brother_age_5_years = brother_age + 5
    result = brother_age_5_years
    return result

print(solution())