def solution():
    """For every 1 year a human ages, a dog ages 7 years.  When Max is 3, how much older, in dog years, will his 3-year-old dog be?"""
    # Define the ratio of human years to dog years
    RATIO = 7

    # Define Max's age in human years
    max_age = 3

    # Calculate Max's dog's age in dog years
    dog_age = max_age * RATIO

    # Calculate how much older the dog is in dog years
    dog_age_diff = dog_age - max_age

    # Display how much older the dog is in dog years
    result = dog_age_diff
    return result

print(solution())