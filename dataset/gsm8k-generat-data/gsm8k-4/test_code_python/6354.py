def solution():
    """Nick is 13 years old. His sister is 6 years older and their brother is half their combined age. How old would their brother be in 5 years?"""
    # Define Nick's age
    nick_age = 13

    # Calculate the sister's age
    sister_age = nick_age + 6

    # Calculate the combined age of Nick and his sister
    combined_age = nick_age + sister_age

    # Calculate the brother's age
    brother_age = combined_age / 2

    # Calculate the brother's age in 5 years
    brother_age_5years = brother_age + 5

    result = brother_age_5years
    return result

print(solution())