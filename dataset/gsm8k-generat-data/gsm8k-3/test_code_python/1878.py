def solution():
    """Emma is 7 years old.  If her sister is 9 years older than her, how old will Emma be when her sister is 56?"""
    # Define Emma's current age and her age difference with her sister
    emma_age = 7
    age_difference = 9

    # Calculate how many years it will take for Emma's sister to be 56
    years_to_56 = 56 - (emma_age + age_difference)

    # Calculate Emma's age at that time
    emma_age_at_56 = emma_age + years_to_56

    # Display Emma's age at that time
    result = emma_age_at_56
    return result

print(solution())