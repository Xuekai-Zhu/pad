def solution():
    
    # Define Cera's current age
    cera_age = 46

    # Calculate Noah's age 6 years ago
    noah_age_6_years_ago = cera_age - 6

    # Calculate Cera's current age
    cera_current_age = cera_age - 6

    # Calculate Noah's current age
    noah_current_age = noah_age_6_years_ago / 2

    # Calculate Chile's current age
    chile_current_age = cera_current_age + noah_current_age

    # Display Chile's current age
    result = chile_current_age
    return result

print(solution())