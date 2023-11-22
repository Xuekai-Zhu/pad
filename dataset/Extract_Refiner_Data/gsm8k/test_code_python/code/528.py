def solution():
    
    # Define Jame's age in 5 years
    jame_age_in_5_years = 27

    # Calculate Jame's current age
    jame_current_age = jame_age_in_5_years - 5

    # Calculate his cousin's age in 8 years
    cousin_age_in_8_years = 2 * jame_current_age - 5

    # Calculate his cousin's current age
    cousin_current_age = cousin_age_in_8_years + 8

    # Calculate the years separate the age of the two
    years_separate = (jame_current_age - cousin_current_age) / 2

    # Display the years separate the age of the two
    result = years_separate
    return result

print(solution())