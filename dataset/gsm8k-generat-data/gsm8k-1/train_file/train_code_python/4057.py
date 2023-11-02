def solution():
    """Tom's brother is 4 times as old as Tom's dog. If in 6 years, Tom's brother will be 30 years, how old is Tom's dog going to be in six years?"""
    brother_age_in_6_years = 30
    dog_to_brother_age_ratio = 1 / 4
    dog_age_in_6_years = brother_age_in_6_years * dog_to_brother_age_ratio - 6
    result = dog_age_in_6_years
    return result

print(solution())