def solution():
    # Find Hania's current age
    hania_age = 45 - 5  # Hania will be 45 years old in 5 years, so her current age is 45 - 5 = 40

    # Find Samir's age
    samir_age = hania_age / 2 + 10  # Samir turned half of Hania's age 10 years ago, so his current age is half of Hania's age now + 10
    samir_age_in_5_years = samir_age + 5  # Find Samir's age in 5 years

    result = samir_age_in_5_years
    return result

print(solution())