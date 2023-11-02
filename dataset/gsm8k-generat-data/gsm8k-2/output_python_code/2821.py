def solution():
    """Jennifer will be 30 years old in ten years. At that time, her sister Jordana will be three times as old Jennifer. How old is Jennifer's sister now?"""
    jennifer_age_in_10_years = 30
    jordana_age_in_10_years = 3 * jennifer_age_in_10_years
    jordana_current_age = jordana_age_in_10_years - 10
    result = jordana_current_age
    return result

print(solution())