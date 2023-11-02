def solution():
    Zion_age = 8
    Dad_age = 4 * Zion_age + 3

    Zion_age_in_10_years = Zion_age + 10
    Dad_age_in_10_years = Dad_age + 10

    age_diff = Dad_age_in_10_years - Zion_age_in_10_years
    result = age_diff
    return result

print(solution())