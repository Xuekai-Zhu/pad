def solution():
    """Gillian’s phone bill is usually $50 a month. If the monthly bill increases by 10%, what will be her phone bill for the entire next year?"""
    monthly_bill = 50
    yearly_increase = 10
    new_monthly_bill = monthly_bill * (1 + yearly_increase / 100)
    new_yearly_bill = new_monthly_bill * 12
    result = new_yearly_bill
    return result

print(solution())