def solution():
    """Christian is twice as old as Brian. In eight more years, Brian will be 40 years old. How old will Christian be in eight years?"""
    # Define Brian's current age
    brian_age = 40 - 8

    # Calculate Christian's current age
    christian_age = brian_age * 2

    # Calculate Christian's age in 8 years
    christian_age_in_8_years = christian_age + 8

    result = christian_age_in_8_years
    return result

print(solution())