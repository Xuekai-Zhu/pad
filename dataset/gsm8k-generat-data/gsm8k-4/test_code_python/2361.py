def solution():
    """Martha met Ellen in the grocery store alone and asked her age. Martha realized she was twice as old as Ellen will be in six years. If Ellen is 10 years old now, calculate Martha's age now."""
    # Define Ellen's current age
    ellen_age = 10

    # Calculate Ellen's age in six years
    ellen_age_six_years = ellen_age + 6

    # Calculate Martha's current age
    martha_age = 2 * ellen_age_six_years - 6

    # return the result
    result = martha_age
    return result

print(solution())