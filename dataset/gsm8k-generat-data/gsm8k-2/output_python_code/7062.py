def solution():
    """Facebook decided to award a productivity bonus to all its female employees who are mothers. This productivity bonus will total 25% of Facebook's annual earnings, which was $5,000,000 for the year 2020. It is known that Facebook employs 3300 employees; one-third are men, and of the women, 1200 are not mothers. How much was the bonus that each female mother employee received, assuming each one received an equal amount?"""
    earnings = 5000000
    bonus_total = 0.25 * earnings
    total_females = (2/3) * 3300
    female_mothers = total_females - 1200
    bonus_per_female_mother = bonus_total / female_mothers
    result = bonus_per_female_mother
    return result

print(solution())