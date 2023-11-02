def solution():
    """Djibo is 17 years old. Five years ago Djibo added his age with his sister's age and the sum was 35. How many years old is Djibo's sister today?"""
    # Djibo's current age
    djibo_age = 17

    # Sum of Djibo's and his sister's ages 5 years ago
    sum_5_years_ago = 35 - 10  # Subtract 10 for 5 years added to each age

    # Djibo's age 5 years ago
    djibo_age_5_years_ago = djibo_age - 5

    # Djibo's sister's age 5 years ago
    sister_age_5_years_ago = sum_5_years_ago - djibo_age_5_years_ago

    # Djibo's sister's current age
    sister_age = sister_age_5_years_ago + 5

    # Display Djibo's sister's current age
    result = sister_age
    return result

print(solution())