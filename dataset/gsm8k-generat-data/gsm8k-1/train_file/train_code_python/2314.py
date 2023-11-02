def solution():
    """Samir just turned half the age Hania was 10 years ago. If in five years Hania will be 45 years old, what will Samir's age be five years from now?"""
    hania_age_now = 45 - 5  # Hania's age now is 45, but we need her age 5 years ago
    hania_age_10_years_ago = hania_age_now - 10
    samir_age_now = hania_age_10_years_ago / 2
    samir_age_5_years_from_now = samir_age_now + 5
    result = samir_age_5_years_from_now
    return result

print(solution())