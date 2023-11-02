def solution():
    """Mel is three years younger than Katherine. When Katherine is two dozen years old, how old will Mel be in years?"""
    # Define Katherine's age when she will be two dozen years old
    katherine_age = 24

    # Calculate Mel's age using Katherine's age
    mel_age = katherine_age - 3

    # Calculate Mel's age when Katherine is two dozen years old
    mel_age_in_2dozen = mel_age + (24 - katherine_age)

    result = mel_age_in_2dozen
    return result

print(solution())