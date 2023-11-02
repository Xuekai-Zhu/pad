def solution():
    """Denise will be 25 years old in two years. Her sister, Diane, is 4 years younger. In how many years will Diane be 25 years old?"""
    # Define Denise's current age
    denise_age = 23

    # Define the age difference between Denise and Diane
    age_diff = 4

    # Calculate Diane's current age
    diane_age = denise_age - age_diff

    # Calculate how many years until Diane is 25 years old
    years = 25 - diane_age

    # Return the result
    result = years
    return result

print(solution())