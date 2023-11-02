def solution():
    """Cadence has worked for her new company five months longer than she worked for her old company. If she worked at her old company for 3 years earning $5000 per month, and she's now earning 20% more in the new company, calculate the total amount of money she's earned in both companies in the period she's worked for them?"""
    # Define the number of months Cadence worked at her old company
    old_company_months = 3 * 12

    # Define Cadence's old salary
    old_salary = 5000

    # Calculate Cadence's earnings at her old company
    old_earnings = old_company_months * old_salary

    # Define the number of months Cadence worked at her new company
    new_company_months = old_company_months + 5

    # Calculate Cadence's new salary (20% more than her old salary)
    new_salary = old_salary * 1.2

    # Calculate Cadence's earnings at her new company
    new_earnings = new_company_months * new_salary

    # Calculate the total amount of money Cadence earned at both companies
    total_earnings = old_earnings + new_earnings

    result = total_earnings
    return result

print(solution())