def solution():
    """Trevor is currently 11 years old and his older brother is 20 years old. How old will Trevor be when his older brother is three times as old as Trevor is now?"""
    # Define Trevor's age and his older brother's age
    trevor_age = 11
    brother_age = 20

    # Calculate the age gap between the two brothers
    age_gap = brother_age - trevor_age

    # Calculate the age at which the older brother will be three times as old as Trevor
    target_age = trevor_age * 3 - age_gap

    # Calculate the number of years until the older brother is three times as old as Trevor
    years_until_target = target_age - brother_age

    # Calculate Trevor's age at the target time
    trevor_age_target = trevor_age + years_until_target

    # Return Trevor's age at the target time
    result = trevor_age_target
    return result

print(solution())