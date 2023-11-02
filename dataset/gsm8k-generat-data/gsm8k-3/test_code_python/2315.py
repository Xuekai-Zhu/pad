def solution():
    """Samir just turned half the age Hania was 10 years ago. If in five years Hania will be 45 years old, what will Samir's age be five years from now?"""
    # Calculate Hania's current age
    hania_age = 45 - 5  # In 5 years, Hania will be 45 years old

    # Calculate Hania's age 10 years ago
    hania_age_10_years_ago = hania_age - 10

    # Calculate Samir's current age
    samir_age = hania_age_10_years_ago * 2

    # Calculate Samir's age in 5 years
    samir_age_in_5_years = samir_age + 5

    # Display Samir's age in 5 years
    result = samir_age_in_5_years
    return result

print(solution())