def solution():
    # Define Nick's age and his sister's age
    nick_age = 13
    sister_age = 13 + 6

    # Calculate the combined age of Nick and his sister
    combined_age = nick_age + sister_age

    # Calculate the age of their brother
    brother_age = 0.5 * combined_age

    # Calculate their brother's age in 5 years
    brother_age_in_5_years = brother_age + 5
    result = brother_age_in_5_years
    return result

print(solution())