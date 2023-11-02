def solution():
    """James turned 23 the same time John turned 35. Tim is 5 years less than twice John's age. If Tim is 79 how old is James?"""
    james_age_diff = 35 - 23
    james_age = 79 - (2 * (35 + 5)) - james_age_diff
    result = james_age
    return result

print(solution())