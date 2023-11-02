def solution():
    """Jon makes 3/4's the salary that Karen makes. John makes $3000 per month. How long will it take him to make the same amount of money that Karen does in 3 months?"""
    # Define Jon's salary and fraction of Karen's salary
    JON_SALARY = 3000
    KAREN_FRACTION = 0.75

    # Calculate Karen's salary for 3 months
    karen_salary = 3 * (JON_SALARY / KAREN_FRACTION)

    # Calculate the time it will take for Jon to make the same amount as Karen
    jon_time = karen_salary / JON_SALARY

    # Display the time in months
    result = jon_time
    return result

print(solution())