def solution():
    """Jennifer will be 30 years old in ten years. At that time, her sister Jordana will be three times as old Jennifer. How old is Jennifer's sister now?"""
    jennifer_age_in_10_years = 30
    sister_age_ratio = 3.0
    sister_age_in_10_years = jennifer_age_in_10_years * sister_age_ratio
    sister_current_age = sister_age_in_10_years - 10
    result = sister_current_age
    return result

print(solution())