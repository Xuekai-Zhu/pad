def solution():
    """Angelina is 4 years older than Justin is now. In 5 years, Angelina will be 40 years old. Calculate the age of Justin currently."""
    # Define Angelina's age in 5 years
    angelina_age_in_5_years = 40

    # Calculate Angelina's current age
    angelina_current_age = angelina_age_in_5_years - 5

    # Calculate Justin's current age
    justin_current_age = angelina_current_age - 4

    # return the result
    result = justin_current_age
    return result

print(solution())