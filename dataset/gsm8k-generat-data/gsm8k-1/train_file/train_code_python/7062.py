def solution():
    """Facebook decided to award a productivity bonus to all its female employees who are mothers. This productivity bonus will total 25% of Facebook's annual earnings, which was $5,000,000 for the year 2020. It is known that Facebook employs 3300 employees; one-third are men, and of the women, 1200 are not mothers. How much was the bonus that each female mother employee received, assuming each one received an equal amount?"""
    total_earnings = 5000000
    bonus_percentage = 25
    bonus_amount = total_earnings * (bonus_percentage / 100)
    total_female_employees = 2/3 * 3300
    total_female_mothers = total_female_employees - 1200
    bonus_per_mother = bonus_amount / total_female_mothers
    result = bonus_per_mother
    return result

print(solution())