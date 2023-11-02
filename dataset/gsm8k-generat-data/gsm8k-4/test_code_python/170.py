def solution():
    """Mel is three years younger than Katherine. When Katherine is two dozen years old, how old will Mel be in years?"""
    # Define Katherine's current age and Mel's current age
    katherine_age = 24
    mel_age = katherine_age - 3

    # Calculate how many years until Katherine is two dozen years old
    years_to_two_dozen = katherine_age - 24

    # Calculate Mel's age when Katherine is two dozen years old
    mel_age_in_two_dozen_years = mel_age + years_to_two_dozen

    # return the result
    result = mel_age_in_two_dozen_years
    return result

print(solution())