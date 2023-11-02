def solution():
    """Leonard is 4 years younger than Nina who is half as old as Jerome. If the sum of their ages is 36, what is Leonard's age?"""
    total_age = 36
    nina_age = total_age * 2 / 5
    jerome_age = nina_age * 2
    leonard_age = nina_age - 4
    result = leonard_age
    return result

print(solution())