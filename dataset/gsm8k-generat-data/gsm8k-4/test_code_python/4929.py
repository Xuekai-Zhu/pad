def solution():
    """John has just turned 39.  3 years ago, he was twice as old as James will be in 6 years.  If James' older brother is 4 years older than James, how old is James' older brother?"""
    # Define John's current age and James' age in 6 years
    john_age = 39
    james_six_years = (john_age - 3) / 2

    # Calculate James' current age and his older brother's age
    james_current = james_six_years - 6
    older_brother = james_current + 4

    # Return the result
    result = older_brother
    return result

print(solution())