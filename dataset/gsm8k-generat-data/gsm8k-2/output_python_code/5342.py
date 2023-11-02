def solution():
    """Gillian’s phone bill is usually $50 a month. If the monthly bill increases by 10%, what will be her phone bill for the entire next year?"""

    monthly_bill = 50
    increase_percentage = 0.1
    yearly_bill = 12 * monthly_bill * (1 + increase_percentage)

    result = yearly_bill
    return result

print(solution())