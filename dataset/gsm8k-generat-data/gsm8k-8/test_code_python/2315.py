def solution():
    # Calculate Hania's current age
    hania_current_age = 45 - 5 

    # Calculate Hania's age 10 years ago
    hania_10_years_ago_age = hania_current_age - 10 

    # Calculate Samir's current age
    samir_current_age = 0.5 * hania_10_years_ago_age

    # Calculate Samir's age in 5 years
    samir_5_years_age = samir_current_age + 5
    result = samir_5_years_age
    return result

print(solution())