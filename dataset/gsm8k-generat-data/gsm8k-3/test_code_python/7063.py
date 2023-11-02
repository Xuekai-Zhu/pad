def solution():
    """Facebook decided to award a productivity bonus to all its female employees who are mothers. This productivity bonus will total 25% of Facebook's annual earnings, which was $5,000,000 for the year 2020. It is known that Facebook employs 3300 employees; one-third are men, and of the women, 1200 are not mothers. How much was the bonus that each female mother employee received, assuming each one received an equal amount?"""
    # Define the total annual earnings and bonus percentage
    ANNUAL_EARNINGS = 5000000
    BONUS_PERCENTAGE = 0.25

    # Calculate the total bonus amount
    female_employees = 2/3*3300  # assuming one-third of employees are men
    female_mothers = female_employees - 1200
    total_bonus = ANNUAL_EARNINGS * BONUS_PERCENTAGE

    # Calculate the bonus amount each female mother employee received
    bonus_per_employee = total_bonus / female_mothers

    # Display the bonus amount each female mother employee received
    result = bonus_per_employee
    return result

print(solution())