def solution():
    # Calculate how much Mrs. Garcia pays for insurance each month
    quarterly_payment = 378
    monthly_payment = quarterly_payment / 3

    # Calculate how much Mrs. Garcia pays for insurance in a year
    yearly_payment = monthly_payment * 12
    result = yearly_payment
    return result

print(solution())