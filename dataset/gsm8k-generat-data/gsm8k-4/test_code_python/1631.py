def solution():
    """John is 10 years old. His sister is twice his age. When he is 50 years old, how old will his sister be?"""
    # Define John's age and his sister's age
    john_age = 10
    sister_age = 2 * john_age

    # Calculate the age difference between John and his sister
    age_diff = sister_age - john_age

    # Add the age difference to John's age when he is 50 to find his sister's age
    sister_age_50 = sister_age + (50 - john_age)

    # Return the sister's age when John is 50
    result = sister_age_50
    return result

print(solution())