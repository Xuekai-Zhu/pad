def solution():
    """If I'm 4 times older than Billy currently, and Billy is 4 years old, how old was I when Billy was born?"""
    # Calculate my current age
    my_age = 4 * 4

    # Calculate the age difference between us
    age_difference = my_age - 4

    # Calculate my age when Billy was born
    my_age_when_billy_was_born = age_difference - 4

    # Return the result
    result = my_age_when_billy_was_born
    return result

print(solution())