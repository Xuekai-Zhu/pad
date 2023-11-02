def solution():
    """John has just turned 39. 3 years ago, he was twice as old as James will be in 6 years. If James' older brother is 4 years older than James, how old is James' older brother?"""
    john_age = 39
    james_future_age = (john_age - 3) / 2 + 6
    james_current_age = james_future_age - 6
    james_older_brother_age = james_current_age + 4
    result = james_older_brother_age
    return result

print(solution())