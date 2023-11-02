def solution():
    # Find Jane's age after 6 years
    jane_age_after_6_years = 28 + 6

    # Find Dara's age after 6 years
    dara_age_after_6_years = jane_age_after_6_years / 2

    # Find how many more years Dara needs to reach the minimum age required
    years_until_hiring = 25 - dara_age_after_6_years
    result = years_until_hiring
    return result

print(solution())