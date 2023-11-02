def solution():
    """James turned 23 the same time John turned 35. Tim is 5 years less than twice John's age. If Tim is 79 how old is James?"""
    john_age = 35
    tim_age = 79
    twice_john_age = (tim_age + 5) / 2
    james_age = john_age - (twice_john_age - 23)
    result = james_age
    return result

print(solution())