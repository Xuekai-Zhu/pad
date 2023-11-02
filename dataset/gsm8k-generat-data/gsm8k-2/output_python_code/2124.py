def solution():
    """For every 1 year a human ages, a dog ages 7 years. When Max is 3, how much older, in dog years, will his 3-year-old dog be?"""
    max_age = 3
    dog_age = max_age * 7
    dog_years_older = dog_age - max_age
    result = dog_years_older
    return result

print(solution())