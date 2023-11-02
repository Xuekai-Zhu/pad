def solution():
    """The total for the sum and product of Elvie's age and Arielle's age are 131. If Elvie's age is 10, how old is Arielle?"""
    elvies_age = 10
    total_age = 131
    arielles_age = (total_age / 2) - elvies_age
    result = arielles_age
    return result

print(solution())