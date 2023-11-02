def solution():
    """For every 1 year a human ages, a dog ages 7 years. When Max is 3, how much older, in dog years, will his 3-year-old dog be?"""
    # Define the age of Max
    max_age = 3

    # Define the age of Max's dog in human years
    dog_age_human = 3

    # Calculate the age of Max's dog in dog years
    dog_age_dog = dog_age_human * 7

    # Calculate how much older Max's dog is in dog years
    dog_age_difference = dog_age_dog - max_age

    result = dog_age_difference
    return result

print(solution())