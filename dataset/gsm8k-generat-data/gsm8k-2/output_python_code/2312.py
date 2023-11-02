def solution():
    """Christian is twice as old as Brian. In eight more years, Brian will be 40 years old. How old will Christian be in eight years?"""
    brian_age_in_8_years = 40
    brian_age_now = brian_age_in_8_years - 8
    christian_age_now = 2 * brian_age_now
    christian_age_in_8_years = christian_age_now + 8
    result = christian_age_in_8_years
    return result

print(solution())