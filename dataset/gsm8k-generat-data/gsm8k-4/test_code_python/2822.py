def solution():
    """Jennifer will be 30 years old in ten years. At that time, her sister Jordana will be three times as old Jennifer. How old is Jennifer's sister now?"""
    # Define Jennifer's age in 10 years
    jennifer_age_in_10_years = 30

    # Calculate Jennifer's current age
    jennifer_current_age = jennifer_age_in_10_years - 10

    # Calculate Jordana's age in 10 years
    jordana_age_in_10_years = jennifer_age_in_10_years * 3

    # Calculate Jordana's current age
    jordana_current_age = jordana_age_in_10_years - 10

    # Return Jordana's current age
    result = jordana_current_age
    return result

print(solution())