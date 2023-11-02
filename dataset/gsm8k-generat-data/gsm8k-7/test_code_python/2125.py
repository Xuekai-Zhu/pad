def solution():
    max_age = 3
    dog_age_multiplier = 7

    # Calculate the age of Max's dog in dog years
    dog_age = max_age * dog_age_multiplier

    # Calculate how much older Max's dog will be in dog years compared to its age in human years
    dog_age_diff = dog_age - max_age
    result = dog_age_diff
    return result

print(solution())