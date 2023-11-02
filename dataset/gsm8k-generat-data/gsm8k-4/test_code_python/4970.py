def solution():
    """5 years ago, a mother was twice as old as her daughter. If the mother is 41 years old now, how old will the daughter be in 3 years?"""
    # Define the current age of the mother
    mother_age = 41

    # Calculate the age of the mother 5 years ago
    mother_age_5_years_ago = mother_age - 5

    # Calculate the age of the daughter 5 years ago
    daughter_age_5_years_ago = mother_age_5_years_ago / 2

    # Calculate the current age of the daughter
    daughter_age = daughter_age_5_years_ago + 5

    # Calculate the age of the daughter in 3 years
    daughter_age_in_3_years = daughter_age + 3

    result = daughter_age_in_3_years
    return result

print(solution())