def solution():
    # Calculate the total amount earned in the old company
    old_company_earnings = 5000 * 36

    # Calculate the number of months worked in the new company
    new_company_months = (36 + 5) * 12

    # Calculate Cadence's new monthly salary
    new_salary = 1.2 * 5000

    # Calculate the total amount earned in the new company
    new_company_earnings = new_salary * new_company_months

    # Calculate the total amount earned in both companies
    total_earnings = old_company_earnings + new_company_earnings
    result = total_earnings
    return result

print(solution())