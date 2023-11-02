def solution():
    # Calculate Katherine's current age
    katherine_age = 2 * 12

    # Calculate Mel's current age
    mel_age = katherine_age - 3

    # Calculate how old Mel will be when Katherine is 2 dozen years old
    mel_age_at_2_dozen = mel_age + (2 * 12 - katherine_age)

    result = mel_age_at_2_dozen
    return result

print(solution())