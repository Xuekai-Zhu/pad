def solution():
    """Tom's brother is 4 times as old as Tom's dog. If in 6 years, Tom's brother will be 30 years, how old is Tom's dog going to be in six years?"""
    # Calculate Tom's brother's current age
    brother_age = 30 - 6
    # brother_age is 24

    # Calculate Tom's dog's current age
    dog_age = brother_age / 4
    # dog_age is 6

    # Calculate Tom's dog's age in 6 years
    dog_age_in_six_years = dog_age + 6

    result = dog_age_in_six_years
    return result

print(solution())