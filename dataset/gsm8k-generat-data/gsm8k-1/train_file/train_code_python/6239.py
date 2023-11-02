def solution():
    """Leonard is 4 years younger than Nina who is half as old as Jerome. If the sum of their ages is 36, what is Leonard's age?"""
    sum_of_ages = 36
    ratio_of_nina_to_jerome = 1/2
    nina_age = (sum_of_ages / (1 + 1 + ratio_of_nina_to_jerome)) * ratio_of_nina_to_jerome
    leonard_age = nina_age - 4
    result = leonard_age
    return result

print(solution())