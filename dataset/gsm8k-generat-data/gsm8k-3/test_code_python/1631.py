def solution():
    """John is 10 years old. His sister is twice his age. When he is 50 years old, how old will his sister be?"""
    # Define John's current age and his sister's current age
    john_age = 10
    sister_age = 2 * john_age

    # Calculate the difference between John's age and 50
    age_difference = 50 - john_age

    # Add the age difference to his sister's current age to get her age when John is 50
    sister_age_at_50 = sister_age + age_difference

    # Display his sister's age when John is 50
    result = sister_age_at_50
    return result

print(solution())