def solution():
    """The total for the sum and product of Elvie's age and Arielle's age are 131. If Elvie's age is 10, how old is Arielle?"""
    elvie_age = 10
    total = 131
    product = 0
    arielle_age = 0
    for i in range(1, total):
        if (i + elvie_age) == (total - i):
            product = i * elvie_age
            arielle_age = i
            break
    result = arielle_age
    return result

print(solution())