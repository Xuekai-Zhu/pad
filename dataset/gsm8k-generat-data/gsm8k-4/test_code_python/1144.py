def solution():
    """Michael has two brothers. His oldest brother is 1 year older than twice Michael's age when Michael was a year younger. His younger brother is 5 years old, which is a third of the age of the older brother. What is their combined age?"""
    # Define the age of Michael's younger brother
    younger_brother_age = 5

    # Calculate the age of Michael's older brother
    older_brother_age = younger_brother_age * 3

    # Calculate Michael's age
    michael_age = older_brother_age / 2 - 1

    # Calculate the combined age of the three brothers
    combined_age = michael_age + older_brother_age + younger_brother_age

    # Return the result
    result = combined_age
    return result

print(solution())