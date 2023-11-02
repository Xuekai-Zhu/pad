def solution():
    """Lexie is 6 years older than her brother and her sister is twice her age. If Lexie is 8, what is the age difference between her brother and her sister?"""
    # Define Lexie's age and calculate her brother's age
    lexie_age = 8
    brother_age = lexie_age - 6

    # Calculate Lexie's sister's age
    sister_age = lexie_age * 2

    # Calculate the age difference between Lexie's brother and sister
    age_difference = sister_age - brother_age

    # Display the age difference
    result = age_difference
    return result

print(solution())