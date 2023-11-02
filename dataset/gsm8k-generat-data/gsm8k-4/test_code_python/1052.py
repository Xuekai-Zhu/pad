def solution():
    """James turned 23 the same time John turned 35. Tim is 5 years less than twice John's age. If Tim is 79 how old is James?"""
    # Calculate the age difference between James and John
    age_diff = 35 - 23

    # Calculate John's current age
    john_age = age_diff + 35

    # Calculate Tim's age
    tim_age = 79

    # Calculate twice John's age
    twice_john_age = 2 * john_age

    # Calculate Tim's age in relation to John's age
    tim_age_john_related = twice_john_age - 5

    # Calculate James' age
    james_age = tim_age_john_related - age_diff

    result = james_age
    return result

print(solution())