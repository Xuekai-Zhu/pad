def solution():
    """John has just turned 39.  3 years ago, he was twice as old as James will be in 6 years. If James' older brother is 4 years older than James, how old is James' older brother?"""
    # Calculate John's age 3 years ago
    john_age_3_years_ago = 39 - 3

    # Calculate James' age in 6 years
    james_age_in_6_years = (john_age_3_years_ago / 2) + 6

    # Calculate James' current age
    james_age_current = james_age_in_6_years - 6

    # Calculate James' older brother's age
    james_older_brother_age = james_age_current + 4

    # Display James' older brother's age
    result = james_older_brother_age
    return result

print(solution())