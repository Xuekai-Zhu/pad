def solution():
    brother_age_in_6_years = 30  # Tom's brother will be 30 years in 6 years
    brother_current_age = brother_age_in_6_years - 6  # Tom's brother's current age
    dog_current_age = brother_current_age / 4  # Tom's dog's current age
    dog_age_in_6_years = dog_current_age + 6  # Tom's dog's age in 6 years

    result = dog_age_in_6_years
    return result

print(solution())