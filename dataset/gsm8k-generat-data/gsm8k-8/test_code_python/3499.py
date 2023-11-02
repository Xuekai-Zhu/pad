def solution():
    # Define the ratio of Isabella's age to Antonio's age
    isabella_to_antonio_ratio = 2

    # Calculate Isabella's current age
    isabella_age = 10 - (18/12)

    # Calculate Antonio's current age using the ratio
    antonio_age = isabella_age / isabella_to_antonio_ratio

    # Calculate Antonio's age in months
    antonio_age_in_months = antonio_age * 12

    result = antonio_age_in_months
    return result

print(solution())