def solution():
    """Kirt has a $6000 monthly salary when he started his job. After a year of working, his salary increased by 30%. How much are his total earnings after 3 years?"""
    # Define the initial salary and the percentage increase
    initial_salary = 6000
    annual_increase = 0.3

    # Calculate the salary after one year
    first_year_salary = initial_salary + (initial_salary * annual_increase)

    # Calculate the total earnings after three years
    total_earnings = first_year_salary * 12 * 3

    # Return the result
    result = total_earnings
    return result

print(solution())