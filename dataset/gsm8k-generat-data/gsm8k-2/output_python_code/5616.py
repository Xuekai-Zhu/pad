def solution():
    """How long is it before Kayla can reach the minimum age of driving of her state, which is 18, if she is currently half the age of her sister Kimiko who is 26 years old?"""
    kimiko_age = 26
    kayla_age = kimiko_age / 2
    years_until_driving_age = 18 - kayla_age
    result = years_until_driving_age
    return result

print(solution())