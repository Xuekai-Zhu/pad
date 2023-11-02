def solution():
    """Emma is 7 years old. If her sister is 9 years older than her, how old will Emma be when her sister is 56?"""
    emma_age = 7
    sister_age_diff = 9
    sister_age = emma_age + sister_age_diff
    years_until_sister_is_56 = 56 - sister_age
    emma_age_when_sister_is_56 = emma_age + years_until_sister_is_56
    result = emma_age_when_sister_is_56
    return result

print(solution())