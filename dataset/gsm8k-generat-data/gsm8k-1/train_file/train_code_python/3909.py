def solution():
    """Mason is three times younger than Sydney and Sydney is six years younger than Mason's father. If Mason is 20 years old, how old is his father?"""
    mason_age = 20
    sydney_age = mason_age * 3
    father_age = sydney_age + 6
    result = father_age
    return result

print(solution())