def solution():
    """Mandy is 3 years old. Her brother is 4 times as old as she is. Her sister is 5 years younger than her brother. What is the age difference between Mandy and her sister?"""
    # Define Mandy's age
    mandy_age = 3

    # Calculate Mandy's brother's age
    brother_age = mandy_age * 4

    # Calculate Mandy's sister's age
    sister_age = brother_age - 5

    # Calculate the age difference between Mandy and her sister
    age_difference = sister_age - mandy_age

    # Return the result
    result = age_difference
    return result

print(solution())