def solution():
    """Cori is 3 years old today.  In 5 years, she will be one-third the age of her aunt.  How old is her aunt today?"""
    # Define Cori's current age
    cori_age = 3

    # Set up the equation
    aunt_age = 3 * (5 + cori_age) - 5

    # Return the aunt's current age
    result = aunt_age
    return result

print(solution())