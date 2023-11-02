def solution():
    """Isabella is twice as old as Antonio. In 18 months, she will be 10 years old. How many months old is Antonio?"""
    # Define Isabella's current age and the age difference between Isabella and Antonio
    isabella_age = 10 * 12 - 18  # convert 10 years to months and subtract 18 months
    age_difference = isabella_age / 2

    # Calculate Antonio's current age
    antonio_age = isabella_age - age_difference

    result = antonio_age
    return result

print(solution())