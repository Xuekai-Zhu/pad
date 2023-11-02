def solution():
    """Samir just turned half the age Hania was 10 years ago. If in five years Hania will be 45 years old, what will Samir's age be five years from now?"""
    # Calculate Hania's current age
    hania_age = 45 - 5  # Hania will be 45 in 5 years from now

    # Calculate Hania's age 10 years ago
    hania_age_10_years_ago = hania_age - 10

    # Calculate Samir's current age
    samir_age = 0.5 * hania_age_10_years_ago

    # Calculate Samir's age in 5 years from now
    samir_age_in_5_years = samir_age + 5

    # Return the result
    result = samir_age_in_5_years
    return result

print(solution())