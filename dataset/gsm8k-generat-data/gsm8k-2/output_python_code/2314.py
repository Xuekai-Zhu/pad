def solution():
    """Samir just turned half the age Hania was 10 years ago. If in five years Hania will be 45 years old, what will Samir's age be five years from now?"""
    hania_age = 45 - 5  # Hania's current age
    hania_age_10_years_ago = hania_age - 10
    samir_age = 0.5 * hania_age_10_years_ago
    samir_age_5_years_from_now = samir_age + 5
    result = samir_age_5_years_from_now
    return result

print(solution())