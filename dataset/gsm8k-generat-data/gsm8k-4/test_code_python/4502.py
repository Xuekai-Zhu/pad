def solution():
    """Arman is six times older than his sister. His sister is 2 years old four years ago. In how many years will Arman's age be 40?"""
    # Define the age of sister 4 years ago
    sister_age_4_years_ago = 2

    # Calculate the age difference between Arman and his sister
    age_difference = 6

    # Calculate the current age of Arman's sister
    sister_age = sister_age_4_years_ago + 4

    # Calculate Arman's current age
    arman_age = sister_age * age_difference

    # Calculate the number of years until Arman's age is 40
    years_until_40 = 40 - arman_age

    # return the result
    result = years_until_40
    return result

print(solution())