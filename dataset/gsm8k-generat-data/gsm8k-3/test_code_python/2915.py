def solution():
    """Adam and Tom are brothers. Adam is 8 years old and Tom is 12 years old. In how many years will their combined age be 44 years old?"""
    # Set up initial ages
    adam_age = 8
    tom_age = 12

    # Set up initial total age
    total_age = adam_age + tom_age

    # Set up years variable
    years = 0

    # Loop until the total age is 44
    while total_age != 44:
        # Increment years and add to age
        years += 1
        adam_age += 1
        tom_age += 1

        # Update total age
        total_age = adam_age + tom_age

    # Display years taken to reach total age of 44
    result = years
    return result

print(solution())