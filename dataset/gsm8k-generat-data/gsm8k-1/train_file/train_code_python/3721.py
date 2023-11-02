def solution():
    """Jorge is 24 years younger than Simon. In 2005, Jorge is 16 years old. In 2010, how old would Simon be?"""
    jorge_age_2005 = 16
    age_difference = 24
    simon_age_2005 = jorge_age_2005 + age_difference
    years_passed = 5
    simon_age_2010 = simon_age_2005 + years_passed
    result = simon_age_2010
    return result

print(solution())