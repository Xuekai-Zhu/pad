def solution():
    """Adam and Tom are brothers. Adam is 8 years old and Tom is 12 years old. In how many years will their combined age be 44 years old?"""
    # Define Adam and Tom's current ages
    adam_age = 8
    tom_age = 12

    # Define the target combined age
    target_combined_age = 44

    # Initialize the year counter
    years = 0

    # Calculate the number of years it will take for their combined age to reach the target
    while adam_age + tom_age != target_combined_age:
        adam_age += 1
        tom_age += 1
        years += 1

    # Return the result
    result = years
    return result

print(solution())