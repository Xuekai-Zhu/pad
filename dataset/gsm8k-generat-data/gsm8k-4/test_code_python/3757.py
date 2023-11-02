def solution():
    """In 5 years, Heath will be 3 times as old as Jude. If Heath is 16 years old today, how old is Jude today?"""
    # Define Heath's current age and the age difference between Heath and Jude
    heath_current_age = 16
    age_difference = 5

    # Use the age difference to calculate Jude's age
    jude_current_age = (heath_current_age - age_difference) / 2

    # Return the result
    result = jude_current_age
    return result

print(solution())