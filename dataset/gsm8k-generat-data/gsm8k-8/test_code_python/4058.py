def solution():
    # Define Tom's brother's current age and the ratio of his age to the dog's age
    brother_age = 30 - 6
    brother_to_dog_ratio = 4

    # Calculate the dog's current age
    dog_age = brother_age / brother_to_dog_ratio

    # Calculate the dog's age in 6 years
    dog_age_in_6_years = dog_age + 6

    result = dog_age_in_6_years
    return result

print(solution())