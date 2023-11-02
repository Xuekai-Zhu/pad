def solution():
    """Facebook decided to award a productivity bonus to all its female employees who are mothers. This productivity bonus will total 25% of Facebook's annual earnings, which was $5,000,000 for the year 2020. It is known that Facebook employs 3300 employees; one-third are men, and of the women, 1200 are not mothers. How much was the bonus that each female mother employee received, assuming each one received an equal amount?"""
    # Define the annual earnings of Facebook and the total number of employees
    ANNUAL_EARNINGS = 5000000
    TOTAL_EMPLOYEES = 3300

    # Calculate the number of female employees who are mothers
    female_employees = (TOTAL_EMPLOYEES/3) * 2  # assuming one-third are men

    # Calculate the bonus amount that each female mother employee received
    bonus_per_employee = (ANNUAL_EARNINGS * 0.25) / (female_employees - 1200)

    result = bonus_per_employee
    return result

print(solution())