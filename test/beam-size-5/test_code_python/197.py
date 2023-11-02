def solution():
    
    # Define the initial time monetary reward and the percentage raise in salary
    INITIAL_REWARD = 5000
    SALARY_PERCENTAGE = 0.05

    # Define the number of weeks in a year
    WEEKS_IN_YEAR = 52

    # Calculate John's salary for the year
    salary_weekly = INITIAL_REWARD * SALARY_PERCENTAGE

    # Calculate John's total earnings for the year
    total_earnings = (INITIAL_REWARD + salary_weekly) * SALARY_PERCENTAGE

    # Display John's total earnings for the year
    result = total_earnings
    return result

print(solution())