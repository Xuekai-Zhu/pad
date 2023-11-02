def solution():
    """Emily has 4 kids named Amy, Jackson, Corey, and James. Amy is 5 years older than Jackson and 2 years younger than Corey. If James is 10 and is 1 year younger than Corey, how old is Jackson?"""
    james_age = 10
    corey_age = james_age + 1
    amy_age = corey_age - 2
    jackson_age = amy_age - 5
    result = jackson_age
    return result

print(solution())