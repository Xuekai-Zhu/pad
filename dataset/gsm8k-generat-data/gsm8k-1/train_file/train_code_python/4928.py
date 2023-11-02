def solution():
    """John has just turned 39. 3 years ago, he was twice as old as James will be in 6 years. If James' older brother is 4 years older than James, how old is James' older brother?"""
    john_age = 39
    james_in_6_years = (john_age - 3) / 2 - 6  # find James' age 3 years ago and subtract 6 from twice his age
    james_age = james_in_6_years + 9  # add 3 to find current age
    brother_age = james_age + 4
    result = brother_age
    return result

print(solution())