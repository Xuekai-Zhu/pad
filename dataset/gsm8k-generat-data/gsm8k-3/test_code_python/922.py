def solution():
    """Cadence has worked for her new company five months longer than she worked for her old company. If she worked at her old company for 3 years earning $5000 per month, and she's now earning 20% more in the new company, calculate the total amount of money she's earned in both companies in the period she's worked for them?"""
    # Define the number of months in a year
    MONTHS_IN_YEAR = 12

    # Define the number of years Cadence worked at her old company
    years_old_company = 3

    # Define Cadence's old monthly salary
    old_salary = 5000

    # Calculate Cadence's total earnings at her old company
    old_earnings = years_old_company * MONTHS_IN_YEAR * old_salary

    # Calculate the number of months Cadence worked at her new company
    months_new_company = years_old_company * MONTHS_IN_YEAR + 5

    # Calculate Cadence's new monthly salary, with a 20% increase
    new_salary = old_salary * 1.2

    # Calculate Cadence's total earnings at her new company
    new_earnings = months_new_company * new_salary

    # Calculate the total earnings for Cadence at both companies
    total_earnings = old_earnings + new_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())