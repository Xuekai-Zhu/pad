def solution():
    """James turned 23 the same time John turned 35.  Tim is 5 years less than twice John's age.  If Tim is 79 how old is James?"""
    # Calculate John's age
    john_age = 35 + (79 - (2 * (35 - 5)))

    # Calculate the age difference between James and John
    age_difference = john_age - 23

    # Calculate James' age
    james_age = 23 + age_difference

    # Display James' age
    result = james_age
    return result

print(solution())