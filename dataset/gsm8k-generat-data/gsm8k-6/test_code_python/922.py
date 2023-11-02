def solution():
    # Calculate Cadence's total earnings from her old company
    old_company_earnings = 3 * 12 * 5000  # Cadence earned $5000 per month for 36 months (3 years)

    # Calculate the number of months Cadence worked for the new company
    new_company_months = 5 + 3 * 12  # Cadence worked for 5 months longer than she worked for her old company

    # Calculate Cadence's earnings from her new company
    new_company_earnings = (1 + 0.2) * 5000 * new_company_months  # Cadence's new salary is 20% more than her old salary

    # Calculate Cadence's total earnings from both companies
    total_earnings = old_company_earnings + new_company_earnings
    result = total_earnings
    return result

print(solution())