def solution():
    """Denise will be 25 years old in two years. Her sister, Diane, is 4 years younger. In how many years will Diane be 25 years old?"""
    # Define Denise's current age and age in two years
    denise_current_age = 23
    denise_future_age = 25

    # Calculate Diane's current age
    diane_current_age = denise_current_age - 4

    # Calculate the number of years until Diane is 25 years old
    years_until_25 = 25 - diane_current_age

    # Display the number of years
    result = years_until_25
    return result

print(solution())