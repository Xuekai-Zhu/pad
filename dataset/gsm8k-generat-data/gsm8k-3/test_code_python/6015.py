def solution():
    """3 years ago James turned 27.  In 5 years Matt will be twice James age.  How old is Matt now?"""
    # Define James' age 3 years ago
    james_age_3_years_ago = 27 - 3

    # Define the age difference between Matt and James
    age_difference = None

    # Find the age difference between Matt and James
    for age_difference_guess in range(1, 100):
        if (james_age_3_years_ago + age_difference_guess + 5) == 2 * (27 + 3 + 5):
            age_difference = age_difference_guess
            break
    
    # Calculate Matt's age
    matt_age = james_age_3_years_ago + age_difference + 5

    # Display Matt's age
    result = matt_age
    return result

print(solution())