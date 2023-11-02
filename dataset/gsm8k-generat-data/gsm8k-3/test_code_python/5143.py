def solution():
    """If I'm 4 times older than Billy currently, and Billy is 4 years old, how old was I when Billy was born?"""
    # Calculate my current age
    my_age = 4 * 4  # Billy's age times the age ratio

    # Subtract Billy's age from my current age to get the age difference
    age_difference = my_age - 4  # Subtract 4 from my age to get my age when Billy was born

    # Display my age when Billy was born
    result = age_difference
    return result

print(solution())