def solution():
    """A family's water and electricity bills average $30 a month for the first 4 months and $24 a month for the last 2 months. If the family's bills were averaged over all 6 months, what would the average monthly bill be?"""
    first_four_months_total = 30 * 4
    last_two_months_total = 24 * 2
    total_spent = first_four_months_total + last_two_months_total
    average_monthly_bill = total_spent / 6
    result = average_monthly_bill
    return result

print(solution())