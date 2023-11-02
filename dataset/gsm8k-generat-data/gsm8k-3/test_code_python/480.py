def solution():
    """Kirt has a $6000 monthly salary when he started his job. After a year of working, his salary increased by 30%. How much are his total earnings after 3 years?"""
    # Define Kirt's starting monthly salary and his salary increase percentage
    STARTING_SALARY = 6000
    INCREASE_PERCENTAGE = 0.3

    # Calculate Kirt's salary after the yearly increase
    yearly_salary = STARTING_SALARY * (1 + INCREASE_PERCENTAGE)

    # Calculate Kirt's total earnings after 3 years
    total_earnings = STARTING_SALARY + yearly_salary * 2 * 12

    # Display Kirt's total earnings
    result = total_earnings
    return result

print(solution())