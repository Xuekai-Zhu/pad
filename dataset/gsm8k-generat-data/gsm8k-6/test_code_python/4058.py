def solution():
    # Find Tom's brother's current age
    brother_age = 30 - 6  # in 6 years, he will be 30 years old
    # Find Tom's dog's current age
    dog_age = brother_age / 4
    # Find Tom's dog's age in 6 years
    dog_age_in_6_years = dog_age + 6
    result = dog_age_in_6_years
    return result

print(solution())