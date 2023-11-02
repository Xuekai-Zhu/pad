def solution():
    """For every 1 year a human ages, a dog ages 7 years. When Max is 3, how much older, in dog years, will his 3-year-old dog be?"""
    max_age = 3
    dog_age = max_age * 7
    dog_age_difference = dog_age - max_age
    result = dog_age_difference
    return result

print(solution())