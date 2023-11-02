def solution():
    """Emma is 7 years old. If her sister is 9 years older than her, how old will Emma be when her sister is 56?"""
    # Define the age difference between Emma and her sister
    age_difference = 9

    # Define Emma's current age
    emma_age = 7

    # Calculate the age difference between Emma and her sister when her sister is 56
    sister_age_at_56 = 56
    sister_age_difference = sister_age_at_56 - emma_age - age_difference

    # Calculate Emma's age when her sister is 56
    emma_age_at_56 = sister_age_at_56 - sister_age_difference

    result = emma_age_at_56
    return result

print(solution())