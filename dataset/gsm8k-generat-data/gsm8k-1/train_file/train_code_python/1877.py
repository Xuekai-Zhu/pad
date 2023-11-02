def solution():
    """Emma is 7 years old. If her sister is 9 years older than her, how old will Emma be when her sister is 56?"""
    emma_age = 7
    age_difference = 9
    sister_age_at_56 = 56
    sister_age_now = sister_age_at_56 - age_difference
    emma_age_at_sisters_age_56 = sister_age_at_56 - emma_age
    emma_age_when_sister_is_56 = emma_age_at_sisters_age_56 + age_difference
    result = emma_age_when_sister_is_56
    return result

print(solution())