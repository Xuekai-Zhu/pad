def solution():
    Arman_sister_age_difference = 6
    sister_initial_age = 2
    years_since_sister_initial_age = 4
    sister_current_age = sister_initial_age + years_since_sister_initial_age
    Arman_current_age = sister_current_age * Arman_sister_age_difference
    years_until_Arman_age_40 = 40 - Arman_current_age
    result = years_until_Arman_age_40
    return result

print(solution())