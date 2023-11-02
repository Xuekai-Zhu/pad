def solution():
    # Calculate Gillian's phone bill for one month after the 10% increase
    monthly_increase = 0.1 * 50
    new_monthly_bill = 50 + monthly_increase

    # Calculate Gillian's phone bill for the entire next year
    yearly_bill = 12 * new_monthly_bill
    result = yearly_bill
    return result

print(solution())